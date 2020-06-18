from django.shortcuts import render
from .models import Movie

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,

    }
    return render(request,'movies/index.html', context)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'title': title,
        'title_en': title_en,
        'audience': audience,
        'open_date': open_date,
        'genre': genre, 
        'watch_grade': watch_grade,
        'score': score,
        'poster_url': poster_url,
        'description': description,

    }
    return render(request, 'movies/detail.html', context)