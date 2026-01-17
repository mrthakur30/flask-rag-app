from query.groq_client import GroqClient
from query.prompt import build_rag_prompt
from query.retriever import retrieve_context


groq_client = GroqClient()


def generate_answer(question: str, top_k: int = 3) -> str:
    context_chunks = retrieve_context(question, top_k)
    prompt = build_rag_prompt(context_chunks, question)
    return groq_client.generate(prompt)
