

from query.generate_answer import generate_answer
from query.retriever import retrieve_context


def rag_agent(question : str) -> str :
    context = retrieve_context(question)

    if not context :
        return "I dont know no relevetn information"
    
    answer = generate_answer(question)

    if "I don't know" in answer:
        return "The knowledge base does not contain this information."
    
    return answer
