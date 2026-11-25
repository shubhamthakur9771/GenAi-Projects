from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Load PDF
loader = PyPDFLoader("document loaders/Acuvate Grooming.pdf")
docs = loader.load()

# Create Prompt Template
template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an AI assistant that summarizes the provided text in a clean and concise way."),
        ("human", "{data}")
    ]
)

# Initialize Mistral Model
model = ChatMistralAI(
    model="mistral-small-2506"
)

# Create Prompt
prompt = template.format_messages(
    data=docs[0].page_content
)

# Invoke Model
result = model.invoke(prompt)

# Print Result
print("\n========= SUMMARY =========\n")
print(result.content)