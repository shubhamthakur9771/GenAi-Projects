# from langchain_community.document_loaders import TextLoader

# data = TextLoader("document loaders/Acuvate Grooming.pdf")
# docs = data.load()
# # print(docs[0].page_content)
# print(len(docs))

# loading pdf documents

from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader("document loaders/Acuvate Grooming.pdf")

docs = data.load()

print(len(docs))
print(docs)

