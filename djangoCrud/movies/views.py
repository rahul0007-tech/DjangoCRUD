from django.shortcuts import render, redirect, get_object_or_404
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
    return render(request, 'listMovie.html', {"movies":movies})

def detailMovie(request, movie_id):
    movie=get_object_or_404(Movie, pk = movie_id)
    return render(request,'detailMovie.html',{"movie":movie})

def updateMovie(request, movie_id):
    movie = get_object_or_404(Movie, pk = movie_id)
    if request.method == "POST":
        movie.image = request.FILES.get('image')
        movie.title = request.POST.get('title')
        movie.director = request.POST.get('director')
        movie.genre = request.POST.get('genre')
        movie.ratings = request.POST.get('ratings')
        movie.description = request.POST.get('description')
        movie.save()
        return redirect('listMovie')
    return render(request, 'updateMovie.html', {'movie': movie})



