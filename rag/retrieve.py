from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "rag/vector_store",
    embeddings,
    allow_dangerous_deserialization=True
)

while True:

    question = input("\nAsk Question (exit to quit): ")

    if question.lower() == "exit":
        break

    docs = db.similarity_search(question, k=2)

    print("\nRetrieved Chunks\n")

    for i, doc in enumerate(docs, start=1):
        print("=" * 60)
        print(f"Chunk {i}")
        print("=" * 60)
        print(doc.page_content)
        print()