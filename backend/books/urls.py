from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.get_books),
    path('books/<int:id>/', views.get_book),
    path('books/add/', views.add_book),
    path('scrape/', views.scrape_books_api),
    path('summary/<int:id>/', views.get_summary),
    path('load-vectors/', views.load_vectors),
    path('ask/', views.ask_question),
    path('insights/<int:id>/', views.get_insights),
    path('recommend/<int:id>/', views.recommend_books),
]