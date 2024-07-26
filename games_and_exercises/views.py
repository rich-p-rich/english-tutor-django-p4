from django.shortcuts import render
from .models import Section

def quiz_level(request, level):
    if request.method == 'POST':
        user_answers = {}
        sections = Section.objects.filter(level=level).prefetch_related('questions__choices')

        for question in questions:
            selected_choice = request.POST.get(str(question.id))
            if selected_choice == question.correct_choice:
                user_answers[question.id] = {'selected': selected_choice, 'correct': True}
            else:
                user_answers[question.id] = {'selected': selected_choice, 'correct': False}

        return render(request, 'exercises.html', {
            'sections': sections,
            'user_answers': user_answers,
            'level': level
        })
    else:
        sections = Section.objects.filter(level=level).prefetch_related('questions__choices')

        return render(request, 'exercises.html', {
            'sections': sections,
            'level': level
        })
