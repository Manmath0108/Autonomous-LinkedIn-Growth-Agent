from langchain_huggingface import HuggingFaceEmbeddings

def get_embeddings():
    """
    Free sentence-transformer embeddings.
    """
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )