from django.shortcuts import render
from django.views.generic.base import View
from .models import Movie

class MovieView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies/base.html', {'movies': movies})

class DetailMovieView(View):
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, 'movies/detail.html', {'movie': movie})


