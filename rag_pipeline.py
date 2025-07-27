
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

def query_knowledge_base(query: str) -> str:
    try:
        embeddings = HuggingFaceEmbeddings()
        vectorstore = FAISS.load_local("kb_index", embeddings, allow_dangerous_deserialization=True)
        docs = vectorstore.similarity_search(query, k=3)
        if not docs:
            return "I wasn’t able to find an answer in the California legal sources I was trained on. For questions about your specific situation, please call the Jury Office at 805-882-4530."
        return "\n\n".join([doc.page_content for doc in docs])
    except:
        raise
