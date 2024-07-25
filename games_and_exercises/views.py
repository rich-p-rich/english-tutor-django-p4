from django.shortcuts import render
from django.http import HttpResponse
from .models import QuizQuestion

def quiz_level(request, level):
    if request.method == 'POST':
        user_answers = {}
        questions = QuizQuestion.objects.filter(level=level)

        for question in questions:
            selected_choice = request.POST.get(str(question.id))
            if selected_choice == question.correct_choice:
                user_answers[question.id] = {'selected': selected_choice, 'correct': True}
            else:
                user_answers[question.id] = {'selected': selected_choice, 'correct': False}

        return render(request, 'exercises.html', {
            'questions': questions,
            'user_answers': user_answers,
            'level': level
        })
    else:
        questions = QuizQuestion.objects.filter(level=level)
        return render(request, 'exercises.html', {
            'questions': questions,
            'level': level
        })