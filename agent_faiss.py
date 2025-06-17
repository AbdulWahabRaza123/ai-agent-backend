import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def ingest_documents(file_path: str, index_dir: str = "faiss_index"):
    print("[INFO] Loading and splitting document...")

    # Load the file (TextLoader works for .txt and .md)
    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()

    # Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)
    print(f"[INFO] Loaded {len(docs)} chunks from {file_path}")

    # Create or update FAISS index
    print("[INFO] Initializing embeddings and FAISS...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    if os.path.exists(index_dir):
        vectorstore = FAISS.load_local(index_dir, embeddings, allow_dangerous_deserialization=True)
        vectorstore.add_documents(docs)
    else:
        vectorstore = FAISS.from_documents(docs, embeddings)

    # Save the index
    vectorstore.save_local(index_dir)
    print(f"[INFO] FAISS index saved to: {index_dir}")

# ✅ Add this for main.py to work
def get_retriever(index_dir: str = "faiss_index"):
    print("[INFO] Loading FAISS index for retrieval...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.load_local(index_dir, embeddings, allow_dangerous_deserialization=True)
    return vectorstore.as_retriever()
