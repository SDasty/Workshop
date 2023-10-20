from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Movie

def home(request, username=None):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm': searchTerm, 'movies': movies, 'username': username})

def about(request, username=None):
    return render(request, 'about.html', {'name': username})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        return redirect('home', username=username)
    return render(request, 'login.html')


