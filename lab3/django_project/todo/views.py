from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import messages
books = {
    '1': {'Author': 'Youssef', 'pages': 50, 'status': False},
    '2': {'Author': 'Ibrahim', 'pages': 40, 'status': False},
    '3': {'Author': 'Salama', 'pages': 90, 'status': False}
}


def todo_home(request, **kwargs):
    print(kwargs)
    the_url_var = kwargs.get('VarToUseInApp')
    print(the_url_var)
    result = books.get(the_url_var)
    return HttpResponse(f"Hello From Django {result}")


def todo_template(request):
    print('true')
    return render(request, 'todo/template.html')


def todo_list(request):
    return render(request, 'todo/todo.html', context={'collection': books})


def todo_details(request, **kwargs):
    the_url_var = kwargs.get('VarToUseInApp')
    print(the_url_var)
    result = books.get(the_url_var)
    return render(request, 'todo/details.html', context={'element': result})


def todo_delete(request, **kwargs):
    the_url_var = kwargs.get('VarToUseInApp')
    print(the_url_var)
    result = books.get(the_url_var)
    if result.get('status'):
        print('ok')
        books.pop(the_url_var)
        return redirect(reverse('todo:list'))
    else:
        print('else')
        return render(request, 'todo/todo.html',
                      context={'warning_msg': "can not delete flase status", 'collection': books})


def todo_state(request, **kwargs):
    book = kwargs.get('VarToUseInApp')
    print(book)
    result = books.get(book)
    result['status'] = True
    print(result)
    print(books)
    return redirect(reverse('todo:list'))


def todo_update(request, **kwargs):
    print(books)
    book = kwargs.get('VarToUseInApp')
    result = books.get(book)
    print(result)
    return render(request, 'todo/todo_update.html', context={'element': result})


def todo_edit(request):
    author = request.POST['author']
    pages = request.POST['pages']
    state = False
    count = len(books.keys())
    books[f"{count + 1}"] = {'Author': author, 'pages': pages, 'status': state}


def todo_add(request):
    print("ok")
    author = request.POST['author']
    pages = request.POST['pages']
    state = False
    # print(author+pages+state)
    count = len(books.keys())
    books[f"{count + 1}"] = {'Author': author, 'pages': pages, 'status': state}
    message="bfbdfbdfb"
    # return render(request, 'todo/todo.html', context={"msg22": "added successfully", 'collection': books})
    messages.success(request, 'Profile details updated.')
    return redirect('todo:list')
