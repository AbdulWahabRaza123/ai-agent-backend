import os
from agent_faiss import ingest_documents

# Path to your data folder
data_folder = "data"

# Gather all .txt and .md files
file_paths = [
    os.path.join(data_folder, f)
    for f in os.listdir(data_folder)
    if f.endswith(".txt") or f.endswith(".md")
]

# Ingest each file
for file_path in file_paths:
    print(f"[INFO] Ingesting: {file_path}")
    ingest_documents(file_path)
