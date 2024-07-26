from django.contrib import admin
from .models import Section, QuizQuestion, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuizQuestionInline(admin.TabularInline):
    model = QuizQuestion
    extra = 1
    inlines = [ChoiceInline]

class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'level')
    inlines = [QuizQuestionInline]

admin.site.register(Section, SectionAdmin)
admin.site.register(QuizQuestion)
admin.site.register(Choice)