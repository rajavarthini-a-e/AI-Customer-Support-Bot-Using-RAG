import os

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

documents = []

folder = "rag/knowledge_base"

for file in os.listdir(folder):

    if file.endswith(".txt"):

        loader = TextLoader(
            os.path.join(folder, file),
            encoding="utf-8"
        )

        documents.extend(loader.load())

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)

vectorstore.save_local("rag/vector_store")

print("Knowledge Base Created Successfully!")
print("Number of Chunks:", len(chunks))