import chromadb
from sentence_transformers import SentenceTransformer

VECTOR_DB_PATH = "vectorstore/chroma_db"
COLLECTION_NAME = "policy_docs"

def test_search(query):
    embed_model = SentenceTransformer("all-MiniLM-L6-v2")

    client = chromadb.Client(
        chromadb.config.Settings(
            persist_directory=VECTOR_DB_PATH
        )
    )

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    query_embedding = embed_model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    for i, doc in enumerate(results["documents"][0]):
        print(f"\nResult {i+1}:")
        print(doc[:500])

if __name__ == "__main__":
    test_search(
        "What are the responsibilities of a Chief Information Security Officer?"
    )
