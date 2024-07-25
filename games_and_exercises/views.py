from django.shortcuts import render, redirect
from .models import Section, QuizQuestion
from .forms import SectionForm, QuizQuestionForm

def create_section(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('section_list')
    else:
        form = SectionForm()
    return render(request, 'create_section.html', {'form': form})

def create_question(request):
    if request.method == 'POST':
        form = QuizQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question_list')
    else:
        form = QuizQuestionForm()
    return render(request, 'create_question.html', {'form': form})

def section_list(request):
    sections = Section.objects.all()
    return render(request, 'section_list.html', {'sections': sections})

def question_list(request):
    questions = QuizQuestion.objects.all()
    return render(request, 'question_list.html', {'questions': questions})
