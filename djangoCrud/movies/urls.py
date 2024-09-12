from django.urls import path
from . import views

urlpatterns = [
    path('addMovie/', views.addMovie),
]
