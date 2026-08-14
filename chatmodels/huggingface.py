import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "YOUR_API_KEY"
llm = HuggingFaceEndpoint(
    repo_id = "deepseek-ai/DeepSeek-R1"
)

model = ChatHuggingFace(llm = llm)

response = model.invoke("Who are you?")

print(response.content)