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
    # generate_answer(docs)
    print(docs[0].page_content)

def generate_answer(text):
    """
    text : supporting passage/text to answer from
    generate the answer from the supported text from vector-db using gpt
    """
    pass