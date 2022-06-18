from django.urls import path
from .views import movies_list, movie_create, movie_detail, movie_delete

app_name = 'movie'

urlpatterns = [
    path('list', movies_list, name='list'),
    path('create', movie_create, name='create'),
    path('<int:pk>/delete', movie_delete, name='delete'),
    path('<int:pk>/detail', movie_detail, name='detail')
]