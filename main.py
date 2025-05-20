import asyncio
import os
import glob
from typing import Dict, List, Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from pydantic import BaseModel

# Import the create-ui tool from tools folder
from tools.create_ui import register_tool

# For vector search
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.http import models

# Load environment variables if needed
from dotenv import load_dotenv

load_dotenv()

# Read from environment
qdrant_mode = os.getenv("QDRANT_MODE", "docker")  # Default to docker
# Option to force re-indexing even if collection exists
force_reindex = os.getenv("FORCE_REINDEX", "false").lower() == "true"


# Initialize the server
app = Server("flyonui-mcp-server")

# Initialize the vector database
model = SentenceTransformer("all-MiniLM-L6-v2")
# Connect to the persistent Qdrant instance running in Docker
if qdrant_mode == "docker":
    # Your existing Docker setup
    qdrant_client = QdrantClient(host="localhost", port=6333)
else:
    # Cloud setup
    qdrant_host = os.getenv("QDRANT_HOST")
    qdrant_api_key = os.getenv("QDRANT_API_KEY")
    qdrant_client = QdrantClient(host=qdrant_host, api_key=qdrant_api_key)

# Collection name for the documentation
COLLECTION_NAME = "flyonui_docs"

# Store component names for later use
ALL_COMPONENT_NAMES = []


# Define the structure for documentation chunks
class DocChunk(BaseModel):
    component: str
    content: str
    path: str
    category: str  # Added category field to track which section the doc belongs to


# Function to load and index documentation
def load_and_index_docs():
    # Check if collection exists
    collections = qdrant_client.get_collections().collections
    collection_names = [collection.name for collection in collections]

    # If collection exists and force_reindex is True, delete the existing collection
    if COLLECTION_NAME in collection_names and force_reindex:
        print(f"Force re-indexing: Deleting existing collection {COLLECTION_NAME}")
        qdrant_client.delete_collection(collection_name=COLLECTION_NAME)
        collection_names.remove(COLLECTION_NAME)

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

        # Load documentation files recursively (now supporting .md files)
        doc_chunks = []
        component_names = []

        # Walk through all subdirectories in the docs folder
        for root, dirs, files in os.walk("docs"):
            # Skip hidden directories
            dirs[:] = [d for d in dirs if not d.startswith(".")]

            # Process markdown files
            for file in files:
                if file.endswith(".md") and not file.startswith("_"):
                    file_path = os.path.join(root, file)

                    # Extract component name (filename without extension)
                    component_name = os.path.splitext(file)[0]

                    # Extract category from directory structure
                    # e.g., docs/components/button.md -> category: components
                    rel_path = os.path.relpath(file_path, "docs")
                    category_parts = os.path.dirname(rel_path).split(os.path.sep)
                    category = (
                        category_parts[0]
                        if category_parts and category_parts[0] != ""
                        else "general"
                    )

                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()

                        # Add component name to our list
                        component_names.append(component_name)

                        # Create a document chunk
                        doc_chunks.append(
                            DocChunk(
                                component=component_name,
                                content=content,
                                path=file_path,
                                category=category,
                            )
                        )
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")

        # Store all component names globally
        global ALL_COMPONENT_NAMES
        ALL_COMPONENT_NAMES = component_names
        print(f"Found {len(ALL_COMPONENT_NAMES)} components")

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
                        "category": chunk.category,
                    },
                )
            )

        # Upload points to the collection
        qdrant_client.upload_points(collection_name=COLLECTION_NAME, points=points)

        print(f"Indexed {len(doc_chunks)} documentation files")
    else:
        print(f"Collection {COLLECTION_NAME} already exists. Skipping indexing.")
        print("To force re-indexing, set FORCE_REINDEX=true environment variable.")


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


# Initialize the documentation index
load_and_index_docs()

# Register the create-ui tool
register_tool(app)


# Run the server
async def main():
    async with stdio_server() as streams:
        await app.run(streams[0], streams[1], app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
