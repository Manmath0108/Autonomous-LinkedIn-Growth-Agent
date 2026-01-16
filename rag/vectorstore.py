from langchain_community.vectorstores import FAISS
from rag.embeddings import get_embeddings

def build_vectorstore(documents):
    embeddings = get_embeddings()
    return FAISS.from_documents(documents, embeddings)