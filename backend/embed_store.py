from backend.ingest import ingest_documents
from sentence_transformers import SentenceTransformer
import chromadb
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
VECTOR_DB_PATH = os.path.join(BASE_DIR, "vectorstore", "chroma_db")
COLLECTION_NAME = "policy_docs"

def create_vector_store():
    documents = ingest_documents()
    embed_model = SentenceTransformer("all-MiniLM-L6-v2")

    client = chromadb.PersistentClient(
        path=VECTOR_DB_PATH
    )

    try:
        client.delete_collection(COLLECTION_NAME)
    except:
        pass

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    texts = []
    metadatas = []
    ids = []

    for doc in documents:
        texts.append(doc["text"])
        metadatas.append({
            "source": doc["source"],
            "chunk_id": doc["chunk_id"]
        })
        ids.append(f'{doc["source"]}_{doc["chunk_id"]}')

    embeddings = embed_model.encode(texts).tolist()

    collection.add(
        documents=texts,
        metadatas=metadatas,
        ids=ids,
        embeddings=embeddings
    )

if __name__ == "__main__":
    create_vector_store()
