from dotenv import load_dotenv

load_dotenv()
from langchain_mistralai import ChatMistralAI
model = ChatMistralAI(model = "mistral-small-2506", temperature=0.9, max_tokens = 20)

# temperature near to one for creative answer and near 0 for logical/reasoning answers
# from langchain.chat_models import init_chat_model

# model = init_chat_model("gpt-4.1")

response = model.invoke("Write a poem on AI")
print(response)