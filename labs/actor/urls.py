from django.urls import path
from .views import actors_list, actor_details, actor_create, actor_update, actor_delete

app_name = 'actor'

urlpatterns = [
    path('list', actors_list, name='list'),
    path('create', actor_create, name='create'),
    path('update/<int:pk>', actor_update, name='update'),
    path('actors/<int:pk>', actor_details, name='detail'),
    path('delete/<int:pk>', actor_delete, name='delete')
]
