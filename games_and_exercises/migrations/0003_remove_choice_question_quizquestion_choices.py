# Generated by Django 4.2.13 on 2024-07-26 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_and_exercises', '0002_alter_quizquestion_correct_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.AddField(
            model_name='quizquestion',
            name='choices',
            field=models.ManyToManyField(related_name='questions', to='games_and_exercises.choice'),
        ),
    ]
