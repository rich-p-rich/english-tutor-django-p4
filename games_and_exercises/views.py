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

        sections = {}
        for question in questions:
            if question.section_title not in sections:
                sections[question.section_title] = []
            choices = []
            for choice in question.choices.all():
                choices.append({
                    'id': choice.id,
                    'text': choice.choice_text,
                    'is_correct': str(choice.id) == question.correct_choice
                })
            sections[question.section_title].append({
                'id': question.id,
                'text': question.question_text,
                'choices': choices
            })

        return render(request, 'exercises.html', {
            'sections': sections,
            'user_answers': user_answers,
            'level': level
        })
    else:
        questions = QuizQuestion.objects.filter(level=level)

        sections = {}
        for question in questions:
            if question.section_title not in sections:
                sections[question.section_title] = []
            choices = []
            for choice in question.choices.all():
                choices.append({
                    'id': choice.id,
                    'text': choice.choice_text,
                    'is_correct': str(choice.id) == question.correct_choice
                })
            sections[question.section_title].append({
                'id': question.id,
                'text': question.question_text,
                'choices': choices
            })

        return render(request, 'exercises.html', {
            'sections': sections,
            'level': level
        })
