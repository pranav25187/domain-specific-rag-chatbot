from transformers import pipeline

def load_llm():
    llm = pipeline(
        "text-generation",
        model="google/flan-t5-base",
        max_new_tokens=256
    )
    return llm
