from django.contrib import admin
from .models import QuizQuestion, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuizQuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(QuizQuestion, QuizQuestionAdmin)