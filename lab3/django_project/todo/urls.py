from django.urls import path

from .views import todo_home, todo_template, todo_list, todo_details, todo_delete, todo_state, todo_add, todo_update

app_name = 'todo'
urlpatterns = [

    path('list', todo_list, name='list'),
    path('tem', todo_template, name='html temp'),
    path('detail/<str:VarToUseInApp>', todo_details, name='todo-detail'),
    path('home/<str:VarToUseInApp>', todo_home, name='todo-home'),
    path('delete/<str:VarToUseInApp>', todo_delete, name='todo-delete'),
    path('state/<str:VarToUseInApp>', todo_state, name='todo-state'),
    path('add', todo_add, name='todo-add'),
    path('update/<str:VarToUseInApp>', todo_update, name='todo-update')
]

# reverse('todo:home') ->/todo/home
