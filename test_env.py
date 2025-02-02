import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="/home/rosh/Desktop/RAG_CHATBOT/.env")

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

print("PINECONE_API_KEY:", PINECONE_API_KEY)
print("GEMINI_API_KEY:", GEMINI_API_KEY)
print("OPENAI_API_KEY:",OPENAI_API_KEY)
