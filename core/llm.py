import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def groq_llm():
    """
    Returns a Groq-backed ChatOpenAI-compatible LLM.
    Centralized LLM factory for all agents.
    """
    return ChatOpenAI(
        model="openai/gpt-oss-20b",
        base_url="https://api.groq.com/openai/v1",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.3,
        max_tokens=1200,
    )