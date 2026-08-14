from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI


model = ChatOpenAI("gpt-4.1")

response = model.invoke("What is cricket")

# print(model)
print(response.content)