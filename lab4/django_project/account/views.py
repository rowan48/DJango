from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm


def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, template_name='registration/signup.html', context={'form': form})