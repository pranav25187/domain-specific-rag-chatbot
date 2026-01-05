import chromadb
from sentence_transformers import SentenceTransformer
from backend.llm_loader import load_llm
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
VECTOR_DB_PATH = os.path.join(BASE_DIR, "vectorstore", "chroma_db")
COLLECTION_NAME = "policy_docs"

SYSTEM_PROMPT = """
You are a domain-specific assistant for IT and Cyber Security policies.
Answer ONLY using the provided context.
If the answer is not present, say:
"I do not have sufficient information in the provided documents."
"""

def get_rag_answer(query: str) -> str:
    embed_model = SentenceTransformer("all-MiniLM-L6-v2")
    llm = load_llm()

    client = chromadb.PersistentClient(
        path=VECTOR_DB_PATH
    )

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    expanded_query = f"""
    {query}
    Chief Information Security Officer CISO responsibilities roles duties
    policy measures nominate CISO cybersecurity team incident response
    """

    query_embedding = embed_model.encode(expanded_query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
    )

    documents = results.get("documents", [[]])[0]

    if not documents:
        return "I do not have sufficient information in the provided documents."

    context = "\n\n".join(documents)

    prompt = f"""
{SYSTEM_PROMPT}

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm(prompt)

    if isinstance(response, list) and "generated_text" in response[0]:
        return response[0]["generated_text"].strip()

    return str(response).strip()
