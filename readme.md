# 🧠 RAG-Based Chat Backend with Flask, LangChain, Gemini & FAISS

This backend project provides a lightweight Retrieval-Augmented Generation (RAG) API that supports chat with memory and a dynamic knowledge base powered by document uploads. It uses:

- [Flask](https://flask.palletsprojects.com/) as the web framework
- [LangChain](https://www.langchain.com/) for orchestration and session memory
- [Gemini](https://ai.google.dev/) for embeddings and response generation
- [FAISS](https://github.com/facebookresearch/faiss) for storing and retrieving document vectors

---

## 🔗 API Endpoints

### 1. `/chat` — Chat with the AI Agent

**Method:** `POST`  
**Description:** Interact with the chatbot by sending a question and a session ID. Each session maintains memory and context.

#### ✅ Request Body

```json
{
  "session_id": "your-unique-session-id",
  "question": "What is this project about?"
}
```
