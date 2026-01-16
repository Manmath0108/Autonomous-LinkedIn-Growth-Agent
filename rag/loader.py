from langchain_core.documents import Document

def load_linkedin_post(path: str):
    """
    Loads LinkedIn posts from a text file.
    Each post must be seperated by:

    \n---\n
    """
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    
    posts = raw.split("\n---\n")

    documents = []
    for post in posts:
        post = post.strip()
        if post:
            documents.append(
                Document(
                    page_content=post,
                    metadat={"source": "linkedin"}
                )
            )
    return documents