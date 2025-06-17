# RAG-Based Chat Backend with Flask, LangChain, Gemini & FAISS

This project is a lightweight Retrieval-Augmented Generation (RAG) API backend that supports AI chat with memory and a dynamic knowledge base. It is ideal for building intelligent assistants that can recall past sessions and incorporate domain-specific knowledge.

---

## Tech Stack

- **Flask** — Lightweight Python web framework for handling API routes
- **LangChain** — Enables session memory and orchestrates RAG logic
- **Gemini** — Powers both embeddings and AI-generated responses
- **FAISS** — Used for storing and retrieving vectorized documents

---

## API Endpoints

### `/chat` — RAG Chat Endpoint

- Accepts a session identifier and a user query.
- Responds with a context-aware answer using Gemini, based on relevant documents retrieved from the FAISS index.
- Each `session_id` maintains its own memory, allowing the assistant to retain context across multiple interactions.

### `/upload` — Knowledge Base Uploader

- Allows the admin to upload `.txt` or `.md` files to the backend.
- Files are processed, embedded via Gemini, and stored in the FAISS index.
- This endpoint dynamically extends the assistant’s knowledge base without needing to restart or redeploy.

---

## Features

- **Session-Aware Conversations**: Memory is maintained per session for a personalized chat experience.
- **Real-Time Knowledge Base Expansion**: Easily update the agent's knowledge via simple document uploads.
- **Efficient Vector Search**: FAISS provides fast retrieval of relevant document chunks.
- **Gemini Integration**: Leverages Gemini both for embedding documents and generating conversational responses.

---

## Project Structure Overview

- `app.py`: Main Flask server and route handler
- `main.py`: Core RAG chat logic
- `agent_faiss.py`: Handles vector storage, document embedding, and FAISS operations
- `data/`: Folder where uploaded documents are saved
- `requirements.txt`: Python dependencies for running the project

---

## 💻 Local Setup Instructions

### Python Version

- This project uses **Python 3.11.2**. Please ensure it is installed before proceeding.

### Setup Steps

1. Create and activate a virtual environment:

   - Use tools like `venv` or `virtualenv` to isolate dependencies.

2. Install all required dependencies:

   - All packages are listed in `requirements.txt`.

3. Run the Flask application:
   - Start the server and begin interacting with the endpoints.

---

## Deployment Notes

This backend relies on FAISS, which requires a writable file system. As a result, platforms with ephemeral or read-only storage (such as Vercel) are **not suitable**.

Recommended environments for deployment:

- Cloud VMs (e.g., AWS EC2, DigitalOcean)
- Docker containers
- Local servers or on-prem hosting

Make sure the `data/` directory is available and has read/write permissions for persistent storage.

---

## CORS Support

Cross-Origin Resource Sharing (CORS) is enabled to allow requests from frontend applications like React or Next.js.

---

## Admin-Only Uploads

The `/upload` endpoint is intended for internal or admin use only. You should secure it with authentication or access controls in a production environment.

---

## Future Enhancements

- Add authentication to secure admin endpoints
- Enable real-time streaming responses via WebSockets
- UI dashboard for uploading and managing documents
- Support for other vector stores like Pinecone or Weaviate

---

## License

## This project is licensed under the **MIT License**.
