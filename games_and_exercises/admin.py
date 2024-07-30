from django import forms
from django.contrib import admin
from .models import Section, QuizQuestion, Choice

class ChoiceInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        correct_choices = 0
        for form in self.forms:
            if not form.cleaned_data.get('DELETE', False) and form.cleaned_data.get('is_correct', False):
                correct_choices += 1
        if correct_choices != 1:
            raise forms.ValidationError('Only one option is correct.')

class ChoiceInline(admin.TabularInline):
    model = Choice
    formset = ChoiceInlineFormSet
    extra = 3
    fields = ['choice_text', 'is_correct']
    templates = 'admin/edit_inline/tabular.html'

class QuizQuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

    class Media:
        js = ('js/.script.js',)

admin.site.register(Section)
admin.site.register(QuizQuestion, QuizQuestionAdmin)
