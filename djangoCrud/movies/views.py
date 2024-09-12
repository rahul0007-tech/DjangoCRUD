from django.shortcuts import render, redirect
from . models import Movie

# Create your views here.
def addMovie(request):
    if request.method == "POST":
        image = request.FILES.get('image')
        title = request.POST.get('title')
        director = request.POST.get('director')
        genre =request.POST.get('genre')
        ratings = request.POST.get('ratings')
        description= request.POST.get('description')

        movie = Movie(image=image, title=title, director=director, genre=genre, ratings=ratings, description=description)
        movie.save()
        return redirect('listMovie')
    
    return render(request, 'addMovie.html')


def listMovie(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {"movies":movies})


