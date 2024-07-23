from django.contrib import admin
from django.urls import path
from games_and_exercises import views

urlpatterns = [
    path('games-and-exercises/', views.quiz, name='games_and_exercises'),
]