from django.shortcuts import render, redirect, reverse
from .models import Movie
from .forms import MovieForm
from django.contrib.auth.decorators import login_required


def movies_list(request):
    return render(request, template_name='movie/movie_list.html', context={'movies': Movie.objects.all()})


def movie_create(request):
    form = MovieForm(data=request.POST or None, files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect('movie:list')

    return render(request, template_name='movie/movie_create.html', context={'form': form})


def movie_detail(request, pk):
    return render(request, template_name='movie/movie_detail.html', context={'movie': Movie.objects.get(pk=pk)})


def movie_delete(request, pk):
    actor = Movie.objects.get(pk=pk)
    actor.delete()
    return redirect(reverse('movie:list'))
