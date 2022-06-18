from django.urls import path
from .views import movies_list, movie_create, movie_detail

app_name = 'movie'

urlpatterns = [
    path('home', movies_list, name='index'),
    path('create', movie_create, name='create'),
    path('<int:pk>/delete', movie_detail, name='delete'),
    path('<int:pk>/detail', movie_detail, name='detail')
]
