# 📘 Domain-Specific RAG Chatbot for IT & Cyber Security Policies

A **domain-specific Retrieval-Augmented Generation (RAG) chatbot** that answers questions strictly based on official **IT and Cyber Security policy documents**.

The system is designed to **prevent hallucinations** by grounding every response in source documents and clearly refusing to answer when information is not available.

---

## 🌐 Live Demo

👉 **Try the application here:**  
https://pranav25187-domain-specific-rag-chatbot-frontendapp-me4nuk.streamlit.app/

---

## 🖼️ Screenshots

<img width="932" height="936" alt="Screenshot 2026-01-05 161644" src="https://github.com/user-attachments/assets/71003efd-bdff-4d0d-859a-c092fee659da" />

---

## 🚀 Key Features

- 📄 PDF-based knowledge ingestion (policy documents)
- ✂️ Intelligent chunking optimized for compliance documents
- 🧠 Semantic search using sentence embeddings
- 🗂️ Persistent vector database with ChromaDB
- 🤖 Retrieval-Augmented Generation (RAG)
- 🚫 Hallucination control (document-grounded answers only)
- 🌐 Interactive Streamlit web interface
- 💯 Fully free & open-source stack

---

## 🏗️ System Architecture

```

Policy PDFs
↓
Text Extraction & Cleaning
↓
Chunking
↓
Embeddings (Sentence Transformers)
↓
ChromaDB (Persistent Vector Store)
↓
Semantic Retriever (Top-K)
↓
LLM (Hugging Face – Free)
↓
Streamlit Web UI

```

---

## 📂 Project Structure

```

domain-llm-chatbot/
│
├── backend/
│   ├── ingest.py
│   ├── embed_store.py
│   ├── rag_chain.py
│   ├── llm_loader.py
│   └── **init**.py
│
├── frontend/
│   └── app.py
│
├── data/
│   └── raw_docs/
│
├── vectorstore/
│   └── chroma_db/
│
├── requirements.txt
├── .gitignore
└── README.md

````

---

## 📑 Document Sources

The chatbot is built using **real-world policy documents**, such as:

- Government Information Security Guidelines (CERT-In)
- Enterprise IT & Cyber Security Policies
- Internal IT governance and compliance documents

⚠️ The assistant answers **only** from these documents.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Sentence Transformers** – semantic embeddings
- **ChromaDB** – persistent vector database
- **Hugging Face Transformers** – free LLM inference
- **Streamlit** – web application framework

---

## ⚙️ Setup Instructions (Local)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/domain-specific-rag-chatbot.git
cd domain-specific-rag-chatbot
````

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📥 Build the Vector Store

Place PDF documents inside:

```
data/raw_docs/
```

Then run:

```bash
python -m backend.embed_store
```

---

## ▶️ Run the Application

```bash
streamlit run frontend/app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 💬 Example Queries

* What are the responsibilities of a Chief Information Security Officer?
* Are employees allowed to use personal laptops?
* What are the compliance requirements for IT security?

If information is not present, the assistant responds safely with:

> *"I do not have sufficient information in the provided documents."*

---

## 🧠 Design Highlights

* Persistent vector storage to avoid data loss
* Absolute path handling for consistent retrieval
* Query expansion for rigid policy language
* Strict prompt rules to prevent hallucinations
* Clean separation of ingestion, retrieval, and UI layers

---

## 🎯 Use Cases

* Enterprise policy assistant
* IT security compliance support
* Audit preparation
* Internal knowledge management systems

---

## 🔒 Security & Privacy

* No API keys committed to the repository
* Secrets managed via environment variables / Streamlit secrets
* Vector database excluded from version control

---

## 📄 License

This project is intended for **educational and portfolio purposes**.

---

## 🙌 Author

**Pranav**
Final-year Computer Engineering student
Focused on **GenAI, RAG systems, and applied machine learning**

```
Just say the word 👌
```
