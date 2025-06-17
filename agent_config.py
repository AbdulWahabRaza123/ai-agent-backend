import os
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
# Load your Gemini API key from env or file
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or "AIzaSyBQqtW5yxNdnAWjtRMp05LVuVJaZxIguJU"

# Use Gemini Flash model (faster, cheaper)
chat_model = ChatGoogleGenerativeAI(
    google_api_key=GOOGLE_API_KEY,
    model="gemini-1.5-flash-latest"
)

# Embedding model
embedding_model = GoogleGenerativeAIEmbeddings(
    google_api_key=GOOGLE_API_KEY,
    model="models/embedding-001"
)
