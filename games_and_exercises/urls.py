from django.contrib import admin
from django.urls import path
from games_and_exercises import views

urlpatterns = [
    path('sections/', views.section_list, name='section_list'),
    path('sections/new/', views.create_section, name='create_section'),
    path('questions/', views.question_list, name='question_list'),
    path('questions/new/', views.create_question, name='create_question'),
    path('quiz/<level>/', views.quiz_level, name='quiz_level'),
]