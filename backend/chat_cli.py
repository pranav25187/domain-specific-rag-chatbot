from backend.rag_chain import get_rag_answer

def chat():
    print("Domain-Specific Policy Assistant (type 'exit' to quit)\n")

    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break

        answer = get_rag_answer(query)
        print("\nAssistant:", answer)
        print("-" * 60)

if __name__ == "__main__":
    chat()
