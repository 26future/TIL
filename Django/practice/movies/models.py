from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    title_en = models.CharField(max_length=50)
    audience = models.CharField(max_length=20)
    open_date = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    watch_grade = models.CharField(max_length=10)
    score = models.CharField(max_length=10)
    poster_url = models.CharField(max_length=500)
    description = models.TextField()
    