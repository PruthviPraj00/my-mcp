import asyncio
import os
import glob
from typing import Dict, List, Any, Union

import mcp.types as types
from mcp.server import Server
from mcp.server.stdio import stdio_server
from pydantic import BaseModel

# For vector search
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.http import models

# Load environment variables if needed
from dotenv import load_dotenv

load_dotenv()

# Initialize the server
app = Server("flyonui-mcp-server")

# Initialize the vector database
model = SentenceTransformer("all-MiniLM-L6-v2")
# Connect to the persistent Qdrant instance running in Docker
qdrant_client = QdrantClient(host="localhost", port=6333)

# Collection name for the documentation
COLLECTION_NAME = "flyonui_docs"

# Store component names for later use
ALL_COMPONENT_NAMES = []


# Define the structure for documentation chunks
class DocChunk(BaseModel):
    component: str
    content: str
    path: str


# Function to load and index documentation
def load_and_index_docs():
    # Check if collection exists
    collections = qdrant_client.get_collections().collections
    collection_names = [collection.name for collection in collections]

    if COLLECTION_NAME not in collection_names:
        print(f"Creating new collection: {COLLECTION_NAME}")
        # Create a new collection
        qdrant_client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=models.VectorParams(
                size=model.get_sentence_embedding_dimension(),
                distance=models.Distance.COSINE,
            ),
        )

        # Load documentation files
        doc_files = glob.glob("docs/*.txt")
        doc_chunks = []
        
        # Store all component names globally
        global ALL_COMPONENT_NAMES
        ALL_COMPONENT_NAMES = [os.path.basename(f).replace(".txt", "") for f in doc_files]
        print(f"Found {len(ALL_COMPONENT_NAMES)} components")

        for file_path in doc_files:
            component_name = os.path.basename(file_path).replace(".txt", "")
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Create a document chunk
            doc_chunks.append(
                DocChunk(component=component_name, content=content, path=file_path)
            )

        # Create embeddings and index documents
        points = []
        for i, chunk in enumerate(doc_chunks):
            embedding = model.encode(chunk.content)
            points.append(
                models.PointStruct(
                    id=i,
                    vector=embedding.tolist(),
                    payload={
                        "component": chunk.component,
                        "content": chunk.content,
                        "path": chunk.path,
                    },
                )
            )

        # Upload points to the collection
        qdrant_client.upload_points(collection_name=COLLECTION_NAME, points=points)

        print(f"Indexed {len(doc_chunks)} documentation files")
    else:
        print(f"Collection {COLLECTION_NAME} already exists. Skipping indexing.")


# Function to search documentation based on a query
def search_docs(query: str, limit: int = 5) -> List[Dict[str, Any]]:
    query_embedding = model.encode(query)
    search_results = qdrant_client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_embedding.tolist(),
        limit=limit,
    )

    results = []
    for result in search_results:
        results.append(
            {
                "component": result.payload["component"],
                "content": result.payload["content"],
                "path": result.payload["path"],
                "score": result.score,
            }
        )

    return results


# Define the create-ui tool
@app.list_tools()
async def list_tools() -> List[types.Tool]:
    return [
        types.Tool(
            name="create-ui",
            description="Generate UI components based on user requirements using FlyonUI. Use this tool when the user requests a new UI component—e.g., mentions /fy, /ui, or asks for a button, input, dialog, table, form, banner, card, or other FlyonUI component.",
            inputSchema={
                "type": "object",
                "properties": {
                    "description": {
                        "type": "string",
                        "description": "Detailed description of the UI component to generate",
                    },
                    "components": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of specific FlyonUI components to include (optional)",
                    },
                },
                "required": ["description"],
            },
            annotations={
                "title": "Create UI Component",
                "readOnlyHint": True,
                "openWorldHint": False,
            },
        )
    ]


@app.call_tool()
async def call_tool(
    name: str, arguments: Dict[str, Any]
) -> List[Union[types.TextContent, types.ImageContent, types.EmbeddedResource]]:
    if name == "create-ui":
        description = arguments.get("description", "")
        components = arguments.get("components", [])

        # Check if the description starts with /fy or /ui and remove the prefix
        if description.startswith("/fy "):
            description = description[4:]
        elif description.startswith("/fy"):
            description = description[3:]
        elif description.startswith("/ui "):
            description = description[4:]
        elif description.startswith("/ui"):
            description = description[3:]
            
        # Identify potential components from the description
        potential_components = []
        
        # Check for component mentions using ALL_COMPONENT_NAMES
        for component in ALL_COMPONENT_NAMES:
            # Skip non-component files like introduction, license, etc.
            if component in ['introduction', 'license', 'quick-start', 'javascript']:
                continue
                
            # Replace hyphens with spaces for natural language matching
            component_name = component.replace('-', ' ')
            
            # Check if component is mentioned in the description
            if component_name in description.lower() or component in description.lower():
                potential_components.append(component)
        
        # Add any explicitly mentioned components
        for component in components:
            if component not in potential_components:
                potential_components.append(component)

        # Search for relevant documentation
        search_query = description
        # Add identified components to the search query
        if potential_components:
            search_query += " " + " ".join(potential_components)
        # Add explicitly specified components
        if components:
            search_query += " " + " ".join(components)
            
        doc_results = search_docs(search_query)

        # Prepare the response with relevant documentation
        response_text = "# FlyonUI Component Generation\n\n"
        response_text += f"## User Request\n{description}\n\n"

        response_text += "## Relevant Documentation\n\n"

        for i, result in enumerate(doc_results):
            component_name = result["component"].replace("-", " ").title()
            response_text += f"### {component_name}\n"

            # Extract the most relevant part of the documentation
            doc_content = result["content"]
            # Limit content to a reasonable size
            max_content_length = 1500
            if len(doc_content) > max_content_length:
                doc_content = (
                    doc_content[:max_content_length]
                    + "...\n(Documentation truncated for brevity)"
                )

            response_text += f"{doc_content}\n\n"

        # Add guidance for implementation
        response_text += "## Implementation Guidance\n\n"
        response_text += "Based on the documentation above, here's how to implement the requested UI component:\n\n"

        # Add example code structure
        response_text += (
            "```html\n<!-- Example structure for the requested component -->\n"
        )

        # If carousel is mentioned in the description, provide a basic carousel template
        if "carousel" in description.lower() or "carousel" in components:
            response_text += """<div class="relative w-full" data-carousel='{ "loadingClasses": "opacity-0" }'>
  <div class="carousel h-80">
    <div class="carousel-body h-full opacity-0">
      <!-- Carousel slides go here -->
      <div class="carousel-slide">
        <!-- Slide content -->
      </div>
      <!-- More slides as needed -->
    </div>
  </div>
  <!-- Navigation buttons -->
  <button class="carousel-prev" type="button">
    <span class="size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
      <span class="icon-[tabler--chevron-left] size-5 cursor-pointer rtl:rotate-180"></span>
    </span>
    <span class="sr-only">Previous</span>
  </button>
  <button class="carousel-next" type="button">
    <span class="sr-only">Next</span>
    <span class="size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
      <span class="icon-[tabler--chevron-right] size-5 cursor-pointer rtl:rotate-180"></span>
    </span>
  </button>
  <!-- Pagination indicators -->
  <div class="carousel-pagination absolute bottom-3 end-0 start-0 flex justify-center gap-3"></div>
</div>"""
        # If team page is mentioned, provide a basic team page structure
        if "team" in description.lower():
            response_text += """<!-- Team Page Structure -->
<div class="container mx-auto px-4 py-8">
  <h1 class="text-3xl font-bold text-center mb-8">Our Team</h1>
  
  <!-- Team description -->
  <div class="max-w-3xl mx-auto text-center mb-12">
    <p class="text-lg text-gray-600">Our talented team of professionals is dedicated to delivering exceptional results.</p>
  </div>
  
  <!-- Team member carousel -->
  <div class="relative w-full" data-carousel='{ "loadingClasses": "opacity-0", "slidesQty": { "xs": 1, "sm": 2, "md": 3, "lg": 4 } }'>
    <div class="carousel h-auto">
      <div class="carousel-body opacity-0 gap-4">
        <!-- Team member cards -->
        <div class="carousel-slide">
          <div class="bg-base-100 rounded-lg shadow-md overflow-hidden">
            <img src="https://source.unsplash.com/random/300x300/?portrait" alt="Team Member" class="w-full h-64 object-cover">
            <div class="p-4">
              <h3 class="text-xl font-semibold">John Doe</h3>
              <p class="text-sm text-gray-500">CEO & Founder</p>
              <p class="mt-2 text-gray-600">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
              <div class="mt-4 flex space-x-3">
                <a href="#" class="text-blue-500"><span class="icon-[tabler--brand-twitter] size-5"></span></a>
                <a href="#" class="text-blue-700"><span class="icon-[tabler--brand-linkedin] size-5"></span></a>
                <a href="#" class="text-gray-700"><span class="icon-[tabler--mail] size-5"></span></a>
              </div>
            </div>
          </div>
        </div>
        <!-- More team members would be added here -->
      </div>
    </div>
    <!-- Navigation buttons -->
    <button class="carousel-prev" type="button">
      <span class="size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
        <span class="icon-[tabler--chevron-left] size-5 cursor-pointer rtl:rotate-180"></span>
      </span>
      <span class="sr-only">Previous</span>
    </button>
    <button class="carousel-next" type="button">
      <span class="sr-only">Next</span>
      <span class="size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
        <span class="icon-[tabler--chevron-right] size-5 cursor-pointer rtl:rotate-180"></span>
      </span>
    </button>
  </div>
</div>"""

        response_text += "\n```\n\n"

        # Add installation instructions
        response_text += "## Installation Instructions\n\n"
        response_text += "To use FlyonUI components, make sure you have the following in your project:\n\n"
        response_text += "1. Tailwind CSS installed and configured\n"
        response_text += "2. FlyonUI installed: `npm install flyonui`\n"
        response_text += (
            "3. Include the necessary JavaScript for interactive components\n"
        )
        response_text += "4. Configure Iconify for Tabler icons: `npm i -D @iconify/tailwind4 @iconify-json/tabler`\n\n"

        response_text += "For more details, refer to the FlyonUI documentation."

        return [types.TextContent(type="text", text=response_text)]

    # If the tool name is not recognized
    return [
        types.TextContent(
            type="text",
            text="Error: Unknown tool. Please use 'create-ui' to generate UI components.",
        )
    ]


# Initialize the documentation index
load_and_index_docs()


# Run the server
async def main():
    async with stdio_server() as streams:
        await app.run(streams[0], streams[1], app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
