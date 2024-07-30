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
        print("question_list view called")  # Initial debug print statement
        print(request.POST)  # Debugging: Print the POST data
        for question in questions:
            selected_choice_id = request.POST.get(str(question.id))
            print(f"Question ID: {question.id}, Selected Choice ID: {selected_choice_id}")  # Debugging: Print question and selected choice IDs
            selected_choice = question.choices.filter(id=selected_choice_id).first() if selected_choice_id else None
            print(f"Selected Choice: {selected_choice}")  # Debugging: Print the selected choice
            user_answers[question.id] = {
                'selected': selected_choice,
                'correct': selected_choice.is_correct if selected_choice else False
            }
            print(f"User Answers: {user_answers[question.id]}")  # Debugging: Print the user answers

    return render(request, 'question-list.html', {
        'section': section,
        'questions': questions,
        'user_answers': user_answers
    })

def all_exercises(request):
    sections = Sections.objects.add().order_by('level')
    return render(request, 'all-exercises.html', {'sections': sections})
