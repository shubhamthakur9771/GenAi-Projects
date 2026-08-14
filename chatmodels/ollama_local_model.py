from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)

response = llm.invoke(
    "What is data science? Explain in 200 words."
)

print(response.content)