import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()

index =  FAISS.load_local("./indexes", embeddings)
def retrive_answer(question):
    """
    question : user query
    search for the answer in the vector-db
    """
    docs = index.similarity_search(question)
    # print(docs[0].page_content)
    answer = generate_answer(docs[0].page_content, question)
    print(answer)
    return answer.content

    

def generate_answer(test, question):
    """
    text : supporting passage/text to answer from
    generate the answer from the supported text from vector-db using gpt
    """
    text = """Supporting Text : \n{}\n\nQuestion{}\n\n Answer:""".format(test, question)
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an AI assistant.\nAnswer the question, only based on the provided supporting text.\nIf answer is not present, in the supporting text, just say, 'sorry I don't have enoough information'"},
        {"role": "user", "content": text}
    ]
    )
    return completion.choices[0].message
    # print(completion.choices[0].message)