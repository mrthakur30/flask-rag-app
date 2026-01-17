def build_rag_prompt(context_chunks: list[str], question: str) -> str:
    context = "\n\n".join(context_chunks)

    prompt = f"""
You are a helpful assistant.
Answer the question using ONLY the context below.
If the answer is not present in the context, say "I don't know".

Context:
{context}

Question:
{question}

Answer:
"""
    return prompt.strip()
