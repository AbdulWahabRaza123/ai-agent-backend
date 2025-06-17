from agent_config import chat_model
from agent_faiss import get_retriever
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

# Retriever (shared across users)
retriever = get_retriever()

# In-memory session tracking
session_chains = {}

def get_qa_chain(session_id: str):
    if session_id not in session_chains:
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer"  # ✅ Fix for multiple outputs
        )
        qa_chain = ConversationalRetrievalChain.from_llm(
            llm=chat_model,
            retriever=retriever,
            memory=memory,
            return_source_documents=True,
            output_key="answer",  # ✅ Declare output key for the chain
            verbose=False
        )
        session_chains[session_id] = qa_chain
    return session_chains[session_id]



def ask_question(session_id: str, question: str):
    qa_chain = get_qa_chain(session_id)
    result = qa_chain.invoke({"question": question})
    return {
        "answer": result["answer"],
        "source_documents": [
            {
                "content": doc.page_content,
                "metadata": doc.metadata
            }
            for doc in result.get("source_documents", [])
        ]
    }

if __name__ == "__main__":
    print("[INFO] Multi-session Chat: Type 'exit' to quit.")
    while True:
        session_id = input("\n🔑 Enter session ID: ").strip()
        if session_id.lower() in ["exit", "quit"]: break

        question = input("🧠 You: ").strip()
        if question.lower() in ["exit", "quit"]: break

        answer = ask_question(session_id, question)
        print("🤖 Gemini:", answer)
