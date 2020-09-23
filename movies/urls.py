from django.urls import path
from .views import MovieView, DetailMovieView

urlpatterns = [
    path('', MovieView.as_view()),
    path('<slug:slug>/', DetailMovieView.as_view()),
]