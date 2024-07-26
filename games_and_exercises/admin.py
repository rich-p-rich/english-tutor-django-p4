from django.contrib import admin
from .models import Section, QuizQuestion, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuizQuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'section', 'correct_choice')
    search_fields = ('question_text',)

class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'level')
    search_fields = ('title', 'level')

admin.site.register(Section, SectionAdmin)
admin.site.register(QuizQuestion, QuizQuestionAdmin)
