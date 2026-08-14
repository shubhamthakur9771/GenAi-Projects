# from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# llm = HuggingFacePipeline.from_model_id(
#     model_id="TinyLlama/TinyLlama-1.1B-Chat-v0.4",
#     task="text-generation",
#     pipeline_kwargs=dict(
#         max_new_tokens = 512,
#         do_sample = False,
#         repetition_penalty = 1.03,
#     ),
# )
# chat_model = ChatHuggingFace(llm = llm)
# result = chat_model.invoke("what is data science")
# print(result.content)


from langchain_huggingface import HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v0.4",
    task="text-generation",
    pipeline_kwargs=dict(
        max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.03,
    ),
)

result = llm.invoke("What is data science? explain in 200 words")

print(result)