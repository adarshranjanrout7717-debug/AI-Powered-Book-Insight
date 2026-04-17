import chromadb
from sentence_transformers import SentenceTransformer
from .models import Book

client = chromadb.Client()
collection = client.get_or_create_collection(name="books")

model = SentenceTransformer('all-MiniLM-L6-v2')


def chunk_text(text, size=100):
    return [text[i:i+size] for i in range(0, len(text), size)]


# ✅ STORE EMBEDDINGS
def store_books_in_vector_db():
    books = Book.objects.all()

    for book in books:
        chunks = chunk_text(book.description or "")

        for i, chunk in enumerate(chunks):
            embedding = model.encode(chunk).tolist()

            collection.add(
                documents=[chunk],
                embeddings=[embedding],
                ids=[f"{book.id}_{i}"]
            )

    return "Stored in vector DB"


# ✅ SEARCH
def search_books(query):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    return results.get('documents', [[]])[0]