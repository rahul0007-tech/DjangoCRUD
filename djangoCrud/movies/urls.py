from django.urls import path
from . import views

urlpatterns = [
    path('addMovie/', views.addMovie, name='addMovie'),
    path('listMovie/', views.listMovie, name='listMovie'),
    path('detailMovie/<int:movie_id>/', views.detailMovie, name='detailMovie'),
    path('updateMovie/<int:movie_id>/', views.updateMovie, name='updateMovie'),
    path('deleteMovie/<int:movie_id>/', views.deleteMovie, name='deleteMovie'),

]
