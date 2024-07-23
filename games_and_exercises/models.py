from django.db import models

class QuizQuestion(models.Model):
    question_text = models.CharField(max_length=255)
    correct_choice = models.CharField(max_length=50)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(QuizQuestion, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=50)

    def __str__(self):
        return self.choice_text