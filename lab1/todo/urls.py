from django.urls import path,include
from .views import  todo_home,get_todo,done_task,delete_task,edit_task,update_task,add_todo,add_task
from . import views


app_name='todo'

urlpatterns = [


    path('',todo_home,name="home"),
    path('home/',todo_home,name="home"),
    path('home/delete/<str:id>',delete_task,name="delete"),
    path('home/done/<str:id>',done_task,name="done"),
    path('home/update/<str:id>', views.update_task, name="update"),
    path('home/edit/<str:id>',edit_task,name="edit"),
    path('home/<str:id>',get_todo,name="todo"),
    path('add/',add_todo,name="add"),
    path('addtask',add_task,name="addtsk")

]
