from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

data = PyPDFLoader("document losders/Acuvate Grooming.pdf")
docs = data.load()
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 10
)
chunks = splitter.split_documents(docs)
pr