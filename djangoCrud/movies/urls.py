from django.urls import path
from . import views

urlpatterns = [
    path('addMovie/', views.addMovie, name='addMovie'),
    path('listMovie/', views.listMovie, name='listMovie'),
    path('detailMovie/<int:movie_id>/', views.detailMovie, name='detailMovie'),
]
