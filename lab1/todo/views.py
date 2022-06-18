from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse



# my_todos={
#     "1":"eat",
#     "2":"sleep",
#     "3":"sleep again"
# }
my_todos = [
	{ "id": 1, "name": "Air Force 1 Mid Casual",  "is_done": False },
	{ "id": 2, "name": "Blazer Mid '77 Casual",  "is_done": False },
	{ "id": 3, "name": "One Take Basketball Shoes", "is_done": False }
]

def todo_home(request):
    context = {'my_todos': my_todos}
    return render(request, 'todo.html', context)

def get_todo(request,**kwargs):
    print("get_todo")
    value = kwargs.get("id")
    del_key = str(value)
    for i in range(len(my_todos)):
        if str(my_todos[i]['id'])==str(del_key):
            print(my_todos[i])
            return HttpResponse(my_todos[i]['name'])


def done_task(request,**kwargs):
    print("done_task")
    value=kwargs.get("is_done")
    value = kwargs.get("id")
    del_key = str(value)
    for i in range(len(my_todos)):
        if str(my_todos[i]['id'])==str(del_key):
            print(my_todos[i])
            my_todos[i]['is_done']=True
            break
    return redirect(reverse('todo:home'))
def delete_task(request,**kwargs):
    print("delete")
    value = kwargs.get("id")
    del_key = str(value)
    for i in range(len(my_todos)):
        if str(my_todos[i]['id'])==str(del_key):
            print(my_todos[i])
            del my_todos[i]
            break


    return redirect(reverse('todo:home'))


def edit_task(request,**kwargs):
    print("edit")
    value = kwargs.get("id")
    del_key = str(value)
    for i in range(len(my_todos)):
        if str(my_todos[i]['id'])==str(del_key):
            print(my_todos[i])
            context = {'my_todo': my_todos[i]}
            return render(request, 'update.html', context)


def update_task(request,**kwargs):
    value = kwargs.get("id")
    body=request.POST["name"]
    print(body)
    print(value)
    del_key = str(value)
    for i in range(len(my_todos)):
        if str(my_todos[i]['id']) == str(del_key):
            my_todos[i].update(name=body)
            context = {'my_todos': my_todos}


    return render(request, 'todo.html', context)
def add_todo(request):
    return render(request,'addTodo.html',context=None)
def add_task(request):
    id=request.POST["id"]
    name=request.POST["name"]
    data={ "id": id, "name": name,  "is_done": False }
    my_todos.insert(len(my_todos),data)
    context = {'my_todos': my_todos}
    return render(request, 'todo.html', context)
