from django.db import models


class Section(models.Model):
    title = models.CharField(max_length=255, default='TBC')
    level = models.CharField(max_length=10, default='TBC')

    def __str__(self):
        return f"{self.title} ({self.level})"


class QuizQuestion(models.Model):
    section = models.ForeignKey(
        Section, related_name='questions', on_delete=models.CASCADE
    )
    question_text = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=50)
    question = models.ForeignKey(
        QuizQuestion, related_name='choices', on_delete=models.CASCADE
    )
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text
