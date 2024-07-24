from django.contrib import admin
from django.urls import path
from games_and_exercises import views

urlpatterns = [
    path('games-and-exercises/<str:level>/', views.quiz_level, name='games_and_exercises'),
]