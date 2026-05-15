
def build_prompt(query, contexts):
    context_block = "\n\n".join(contexts) if contexts else "(no relevant context found)"
    prompt = (
        "You are a helpful AI assistant. Use the context below to answer.\n\n"
        f"Context:\n{context_block}\n\n"
        f"Question: {query}\n"
        "Answer:"
    )
    return prompt
