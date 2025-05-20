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
        ALL_COMPONENT_NAMES = [
            os.path.basename(f).replace(".txt", "") for f in doc_files
        ]
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
