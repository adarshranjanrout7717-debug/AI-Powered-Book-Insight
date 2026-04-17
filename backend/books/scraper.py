import requests
from bs4 import BeautifulSoup
from .models import Book

def scrape_books():
    url = "http://books.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.find_all('article', class_='product_pod')

    for book in books[:10]:  # limit to 10 books
        title = book.h3.a['title']
        rating_class = book.p['class'][1]

        rating_map = {
            "One": 1, "Two": 2, "Three": 3,
            "Four": 4, "Five": 5
        }

        rating = rating_map.get(rating_class, 0)

        # Save to DB
        Book.objects.create(
            title=title,
            author="Unknown",
            description="Sample scraped book",
            rating=rating,
            url=url
        )

    return "Books scraped successfully!"