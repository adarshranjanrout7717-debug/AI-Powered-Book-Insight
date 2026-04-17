from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from .scraper import scrape_books
from .ai_utils import generate_summary
from .rag import store_books_in_vector_db, search_books
from .ai_utils import generate_summary
from django.core.cache import cache

# GET all books
@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

# GET single book
@api_view(['GET'])
def get_book(request, id):
    book = Book.objects.get(id=id)
    serializer = BookSerializer(book)
    return Response(serializer.data)

# POST new book
@api_view(['POST'])
def add_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)



@api_view(['GET'])
def scrape_books_api(request):
    result = scrape_books()
    return Response({"message": result})



@api_view(['GET'])
def get_summary(request, id):
    try:
        book = Book.objects.get(id=id)
        summary = generate_summary(book.description)
        return Response({
            "title": book.title,
            "summary": summary
        })
    except Book.DoesNotExist:
        return Response({"error": "Book not found"})
    


@api_view(['GET'])
def load_vectors(request):
    result = store_books_in_vector_db()
    return Response({"message": result})


@api_view(['POST'])
def ask_question(request):
    query = request.data.get("question")

    docs = search_books(query)
    context = " ".join(docs)

    answer = generate_summary(context + "\n" + query)

    return Response({
        "question": query,
        "answer": answer,
        "source": docs
    })    

@api_view(['GET'])
def get_insights(request, id):
    try:
        book = Book.objects.get(id=id)

        genre = classify_genre(book.description)
        sentiment = analyze_sentiment(book.description)

        book.genre = genre
        book.sentiment = sentiment
        book.save()

        return Response({
            "title": book.title,
            "genre": genre,
            "sentiment": sentiment
        })

    except:
        return Response({"error": "Something went wrong"})
    
@api_view(['GET'])
def recommend_books(request, id):
    try:
        book = Book.objects.get(id=id)

        # Use RAG search
        docs = search_books(book.description)

        return Response({
            "recommendations": docs
        })

    except Exception as e:
        return Response({"error": str(e)}) 
    

@api_view(['GET'])
def get_summary(request, id):
    cache_key = f"summary_{id}"
    cached = cache.get(cache_key)

    if cached:
        return Response({"summary": cached})

    book = Book.objects.get(id=id)
    summary = generate_summary(book.description)

    cache.set(cache_key, summary, timeout=3600)

    return Response({"summary": summary})    