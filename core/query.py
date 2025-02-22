
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_community.vectorstores import FAISS
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI

from core.history import History
from core.reader import document_embeddings


def most_similar(path, query):
    new_db = FAISS.load_local(path, document_embeddings, allow_dangerous_deserialization=True)
    docs_with_score = new_db.similarity_search_with_score(query)
    return docs_with_score[0]


def langchain_history(history: History):
    logs = []
    for log in history.logs:
        if log["role"] == "user":
            logs.append(HumanMessage(log["content"]))
        elif log["role"] == "assistant":
            logs.append(AIMessage(log["content"]))
        elif log["role"] == "system":
            logs.append(SystemMessage(log["content"]))
    return logs


def query_document(pages, query, model="gpt-4o", history=None):
    if len(pages) > 166:
        pages = pages[:165]  # max buffer size
    if history is None:
        history = History()
    print(len(pages))
    vectorstore = FAISS.from_documents(pages, document_embeddings)

    chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(temperature=0.0, model_name=model),
        retriever=vectorstore.as_retriever(),
    )
    logs = langchain_history(history)
    chat = chain.invoke({"question": query, "chat_history": logs})["answer"]
    return chat
