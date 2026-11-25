from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model = "mistral-small-2506", temperature=0.9)
print("-----Welcome, press 0 to end the chat------")
while True:
    prompt = input("You: ")
    if prompt == "0":
        break
    response = model.invoke(prompt)
    print("Bot: " ,response.content)
