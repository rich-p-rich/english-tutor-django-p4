from django.shortcuts import render
from .models import Section, QuizQuestion

def section_list(request, level):
    sections = Section.objects.filter(level=level)
    return render(request, 'section-list.html', {'sections': sections, 'level': level})

def question_list(request, section_id):
    section = Section.objects.get(id=section_id)
    questions = section.questions.prefetch_related('choices').all()
    if request.method == 'POST':
        user_answers = {}
        for question in questions:
            selected_choice = request.POST.get(str(question.id))
            if selected_choice == question.correct_choice:
                user_answers[question.id] = {'selected': selected_choice, 'correct': True}
            else:
                user_answers[question.id] = {'selected': selected_choice, 'correct': False}

        return render(request, 'question-list.html', {
            'section': section,
            'questions': questions,
            'user_answers': user_answers
        })
    else:
        return render(request, 'question-list.html', {
            'section': section,
            'questions': questions
        })
