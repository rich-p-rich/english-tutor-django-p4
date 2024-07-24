from django.db import models

class QuizQuestion(models.Model):
    question_text = models.CharField(max_length=255)
    correct_choice = models.CharField(max_length=50)
    level = models.CharField(max_length=10, default='TBC')
    # The level field categorizes the questions by difficulty
    # The level is set to TBC(to be confirmed) as a default placeholder text

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(QuizQuestion, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=50)

    def __str__(self):
        return self.choice_text