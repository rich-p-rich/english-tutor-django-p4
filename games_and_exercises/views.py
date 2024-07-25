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

        question_data = []
        previous_section_title = None
        for question in questions:
            choices = []
            for choice in question.choices.all():
                choices.append({
                    'id': choice.id,
                    'text': choice.choice_text,
                    'is_correct': str(choice.id) == question.correct_choice
                })
            question_data.append({
                'id': question.id,
                'text': question.question_text,
                'choices': choices,
                'section_title': question.section_title,
                'show_section_title': question.section_title != previous_section_title
            })
            previous_section_title = question.section_title

        return render(request, 'exercises.html', {
            'questions': question_data,
            'user_answers': user_answers,
            'level': level
        })
    else:
        questions = QuizQuestion.objects.filter(level=level)

        question_data = []
        previous_section_title = None
        for question in questions:
            choices = []
            for choice in question.choices.all():
                choices.append({
                    'id': choice.id,
                    'text': choice.choice_text,
                    'is_correct': str(choice.id) == question.correct_choice
                })
            question_data.append({
                'id': question.id,
                'text': question.question_text,
                'choices': choices,
                'section_title': question.section_title,
                'show_section_title': question.section_title != previous_section_title
            })
            previous_section_title = question.section_title

        return render(request, 'exercises.html', {
            'questions': question_data,
            'level': level
        })