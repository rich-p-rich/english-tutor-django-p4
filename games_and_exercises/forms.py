from django import forms
from .models import Section, QuizQuestion


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['title']


class QuizQuestionForm(forms.ModelForm):
    class Meta:
        model = QuizQuestion
        fields = ['section', 'question_text', 'correct_choice', 'level']
