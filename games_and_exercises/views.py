from django.shortcuts import render, get_object_or_404
from .models import Section, QuizQuestion, Choice

def section_list(request, level):
    sections = Section.objects.filter(level=level)
    return render(request, 'section-list.html', {'sections': sections, 'level': level})

def question_list(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    questions = section.questions.prefetch_related('choices').all()
    user_answers = {}

    if request.method == 'POST':
        for question in questions:
            selected_choice_id = request.POST.get(str(question.id))
            selected_choice = question.choices.filter(id=selected_choice_id).first() if selected_choice_id else None
            user_answers[question.id] = {
                'selected': selected_choice,
                'correct': selected_choice == question.correct_choice if selected_choice else False
            }

    return render(request, 'question-list.html', {
        'section': section,
        'questions': questions,
        'user_answers': user_answers
    })

def all_exercises(request):
    sections = Sections.objects.add().order_by('level')
    return render(request, 'all-exercises.html', {'sections': sections})
