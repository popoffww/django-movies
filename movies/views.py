from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Movie

# class MovieView(View):
#     def get(self, request):
#         movies = Movie.objects.all()
#         return render(request, 'movies/movies.html', {'movie_list': movies})
#
# class DetailMovieView(View):
#     def get(self, request, slug):
#         movie = Movie.objects.get(url=slug)
#         return render(request, 'movies/movie_detail.html', {'movie': movie})


class MovieListView(ListView):
    model = Movie
    queryset = Movie.objects.all()

class MovieDetailView(DetailView):
    model = Movie
    slug_field = 'url'