from langchain.vectorstores import FAISS
from langchain.schema import Document
import pandas as pd
from langchain_openai import OpenAIEmbeddings

from core.chatgpt import llm_chat
from core.history import History


def dict_to_str(row):
    text = ""
    for key, item in row.items():
        text += str(key) + ": " + str(item) + " "
    return text


if __name__ == "__main__":

    grants = pd.read_csv("data/us_government_grants.csv")
    applicants = pd.read_csv("data/grant_applicants.csv")

    selected_index = 5
    # Convert each row into a document
    members = []
    for index, row in grants.iterrows():

        content = dict_to_str(row)
        members.append(Document(page_content=content))

    # Initialize embeddings and FAISS database
    embeddings = OpenAIEmbeddings()
    vector_db = FAISS.from_documents(members, embeddings)

    # Example: Find closest members for the first person
    print(applicants)
    query = dict_to_str(applicants.iloc[selected_index])
    print("1 ", query)

    closest_grant = vector_db.similarity_search(query)[0]
    print("2 ", closest_grant.page_content)

    history = History()
    history.system("You are a AI community manager that helps to grow the community and connect memobers to each other.")
    history.system("Applicant: " + query)
    history.system("Grant: " + closest_grant.page_content)
    history.user("Write a motivation why Applicant should explore funding options from Grant.")
    print(llm_chat(history))