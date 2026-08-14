from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
model = ChatOllama(
    model="qwen2.5:3b",
    temperature=0.9
)
messages = [
  SystemMessage(content="You are a funny Ai agent")
]

print("-----Welcome, press 0 to end the chat------")

while True:
    prompt = input("You: ")
    messages.append(HumanMessage(content=prompt))

    if prompt == "0":
        break

    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))

    print("Bot:", response.content)
print(messages)