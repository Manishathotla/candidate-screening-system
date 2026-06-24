from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

PDF_PATH = "knowledge_base/ml_book.pdf"

CHROMA_PATH = "chroma_db"


def create_vector_db():

    print("Loading PDF...")

    loader = PyPDFLoader(PDF_PATH)

    documents = loader.load()

    print("Chunking documents...")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    print(f"Total Chunks: {len(chunks)}")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )

    print("Vector database created successfully")


if __name__ == "__main__":
    create_vector_db()