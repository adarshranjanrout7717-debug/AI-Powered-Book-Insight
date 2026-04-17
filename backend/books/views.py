from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache

from .models import Book
from .serializers import BookSerializer
from .scraper import scrape_books
from .ai_utils import (
    generate_summary,
    classify_genre,
    analyze_sentiment
)
from .rag import store_books_in_vector_db, search_books


# -------------------------------
# GET ALL BOOKS
# -------------------------------
@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


# -------------------------------
# GET SINGLE BOOK
# -------------------------------
@api_view(['GET'])
def get_book(request, id):
    try:
        book = Book.objects.get(id=id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"})


# -------------------------------
# ADD BOOK
# -------------------------------
@api_view(['POST'])
def add_book(request):
    serializer = BookSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)


# -------------------------------
# SCRAPE BOOKS
# -------------------------------
@api_view(['GET'])
def scrape_books_api(request):
    result = scrape_books()
    return Response({"message": result})


# -------------------------------
# GET SUMMARY
# -------------------------------
@api_view(['GET'])
def get_summary(request, id):
    try:
        cache_key = f"summary_{id}"
        cached = cache.get(cache_key)

        book = Book.objects.get(id=id)

        if cached:
            return Response({
                "title": book.title,
                "summary": cached
            })

        text = book.description if book.description else book.title

        summary = generate_summary(text)

        if not summary or "not available" in summary.lower():
            summary = text[:250]

        cache.set(cache_key, summary, timeout=3600)

        return Response({
            "title": book.title,
            "summary": summary
        })

    except Book.DoesNotExist:
        return Response({"error": "Book not found"})


# -------------------------------
# LOAD VECTORS
# -------------------------------
@api_view(['GET'])
def load_vectors(request):
    result = store_books_in_vector_db()
    return Response({"message": result})


# -------------------------------
# ASK AI (RAG)
# -------------------------------
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


# -------------------------------
# INSIGHTS
# -------------------------------
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


# -------------------------------
# RECOMMENDATIONS
# -------------------------------
@api_view(['GET'])
def recommend_books(request, id):
    try:
        book = Book.objects.get(id=id)

        docs = search_books(book.description)

        return Response({
            "recommendations": docs
        })

    except Exception as e:
        return Response({"error": str(e)})