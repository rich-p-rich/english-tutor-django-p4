from django.db import models

class Section(models.Model):
    title = models.CharField(max_length=255, default='TBC')
    level = models.CharField(max_length=10, default='TBC')

    def __str__(self):
        return f"{self.title} ({self.level})"

class QuizQuestion(models.Model):
    section = models.ForeignKey(Section, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    correct_choice = models.CharField(max_length=50)
    # The level field categorizes the questions by difficulty
    # The level is set to TBC(to be confirmed) as a default placeholder text

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(QuizQuestion, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=50)

    def __str__(self):
        return self.choice_text