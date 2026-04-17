from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.FloatField(null=True, blank=True)
    url = models.URLField()
    genre = models.CharField(max_length=100, blank=True, null=True)
    sentiment = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title