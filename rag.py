from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


CHROMA_PATH = "chroma_db"


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


db = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=embeddings
)


def retrieve_context(query):

    results = db.similarity_search(
        query,
        k=3
    )

    context = ""

    for doc in results:
        context += doc.page_content + "\n"

    return context