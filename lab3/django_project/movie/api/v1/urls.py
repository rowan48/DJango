from django.urls import path
from .views import hello_drf, movie_list, Movielist, movie_detail, movie_create, movie_update, MovieUpdate, movie_delete

app_name = 'api'
urlpatterns = [
    path('hello-drf', hello_drf, name='ho-drf'),
    path('list', movie_list, name='list'),
    path('generic', Movielist.as_view(), name='generic-list'),
    path('<int:movie_id>', movie_detail, name='details'),
    path('create', movie_create, name='create'),
    path('update/<int:movie_id>', movie_update, name='update'),
    path('update/generic', MovieUpdate.as_view(), name='generic-update'),
    path('delete/<int:movie_id>', movie_delete, name='generic-delete'),
]
