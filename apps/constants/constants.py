from dotenv import load_dotenv
import os

load_dotenv()

SERVER_URL = "localhost"
PORT = "8900"
ENV = "dev"
# uvicorn main:app --host 0.0.0.0 --port 80
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
