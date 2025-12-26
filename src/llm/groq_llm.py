from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

class GroqLLM:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("Missing GROQ_API_KEY")
        self.llm = ChatGroq(api_key=self.api_key, model="llama-3.1-8b-instant")

    def get_response(self, user_input: str):
        return self.llm.invoke(user_input).content
