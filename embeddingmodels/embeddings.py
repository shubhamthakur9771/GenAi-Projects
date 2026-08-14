# from langchain_openai import OpenAIEmbeddings
# from dotenv import load_dotenv

# load_dotenv()
# embeddings = OpenAIEmbeddings(
#     model='text-embedding-3-large',
#     dimensions=64
# )



# vector = embeddings.embed_query("you are going to learn gen ai")
# print(vector)


from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

texts = [
    "hello this is shubham",
    "hello your name is youtube",
    "you are very smart"
]

vectors = embeddings.embed_documents(texts)

print(vectors[0][:5])

