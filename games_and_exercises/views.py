from django.shortcuts import render
from django.http import HttpResponse
from .models import QuizQuestion

def quiz(request):
    if request.method == 'POST':
        correct_answers = 0
        total_questions = QuizQuestion.objects.count()
        user_answers = {}

        for question in QuizQuestion.objects.all():
            selected_choice = request.POST.get(str(question.id))
            if selected_choice == question.correct_choice:
                correct_answers += 1
                user_answers[question.id] = {'selected': selected_choice, 'correct': True}
            else:
                user_answers[question.id] = {'selected': selected_choice, 'correct': False}

        score = (correct_answers / total_questions) * 100
        return render(request, 'games-and-exercises.html', {
            'questions': QuizQuestion.objects.all(),
            'user_answers': user_answers,
            'score': score
        })
    else:
        return render(request, 'games-and-exercises.html', {'questions': QuizQuestion.objects.all()})
    