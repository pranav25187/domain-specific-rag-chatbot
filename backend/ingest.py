import os
from utils.pdf_loader import load_pdf_text
from utils.text_cleaner import clean_text
from langchain_text_splitters import RecursiveCharacterTextSplitter


RAW_DOCS_PATH = "data/raw_docs"
PROCESSED_PATH = "data/processed_docs"

os.makedirs(PROCESSED_PATH, exist_ok=True)

def ingest_documents():
    all_chunks = []

    splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50,
    separators=["\n\n", "\n", ".", " "]
)


    for filename in os.listdir(RAW_DOCS_PATH):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(RAW_DOCS_PATH, filename)

            print(f"Processing: {filename}")

            raw_text = load_pdf_text(pdf_path)
            cleaned_text = clean_text(raw_text)

            chunks = splitter.split_text(cleaned_text)

            for i, chunk in enumerate(chunks):
                all_chunks.append({
                    "source": filename,
                    "chunk_id": i,
                    "text": chunk
                })

    print(f"Total chunks created: {len(all_chunks)}")
    return all_chunks


if __name__ == "__main__":
    ingest_documents()
