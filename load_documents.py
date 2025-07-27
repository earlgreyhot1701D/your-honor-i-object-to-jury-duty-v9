
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def build_faiss_index():
    documents = []
    for filename in os.listdir("docs"):
        if filename.endswith(".txt"):
            loader = TextLoader(os.path.join("docs", filename), encoding="utf-8")
            documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    splits = splitter.split_documents(documents)
    embeddings = HuggingFaceEmbeddings()
    vectorstore = FAISS.from_documents(splits, embeddings)
    vectorstore.save_local("kb_index")

if __name__ == "__main__":
    build_faiss_index()
