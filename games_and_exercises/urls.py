from django.urls import path
from .views import past_tense_1
urlpatterns = [
    path('games-and-exercises/', past_tense_1, name='games_and_exercises'),
]