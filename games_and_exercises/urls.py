from django.contrib import admin
from django.urls import path
from games_and_exercises import views

urlpatterns = [
        path('exercises/<str:level>/', views.quiz_level, name='quiz_level'),
]