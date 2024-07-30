from django.contrib import admin
from django.urls import path
from games_and_exercises import views

urlpatterns = [
    path('sections/<str:level>/', views.section_list, name='section_list'),
    path('section/<int:section_id>/', views.question_list, name='question_list'),
    path('all-exercises/', views.all_exercises, name='all_exercises'),
]