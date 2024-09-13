from django.db import models

# Create your models here.

class Movie(models.Model):
    image = models.ImageField(upload_to='movies/')
    title = models.CharField(max_length=20)
    director = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    ratings = models.IntegerField()
    releaseDate = models.DateField(blank=True)
    description = models.CharField(max_length=100)

    def __str__ (self):
        return self.title
