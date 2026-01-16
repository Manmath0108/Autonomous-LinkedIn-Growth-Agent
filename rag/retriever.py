from rag.loader import load_linkedin_post
from rag.splitter import split_documents
from rag.vectorstore import build_vectorstore

def get_retriever():
    """
    Builds and returns a retriever over LinkedIn posts
    """
    documents = load_linkedin_post("data/linkedin_posts.txt")
    documents = split_documents(documents)

    vectorstore = build_vectorstore(documents)

    return vectorstore.as_retriever(
        search_kwargs={"k":5}
    )