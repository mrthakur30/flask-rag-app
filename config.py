import os 
from dotenv import load_dotenv

load_dotenv();

class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    TOP_K = int(os.getenv("TOP_K", 3))
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 500))