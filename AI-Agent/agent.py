import ollama

SYSTEM_PROMPT = """
You are an AI Agent.
You think step by step before answering.
Always break down the problem, reason, then answer clearly.
"""

def agent(question):
    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ]
    )
    return response["message"]["content"]


if __name__ == "__main__":
    print("Simple Ollama AI Agent (type 'exit' to quit)\n")

    while True:
        q = input("You: ")
        if q.lower() == "exit":
            break

        answer = agent(q)
        print("\nAgent:\n", answer, "\n")
