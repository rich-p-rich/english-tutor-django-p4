# Generated by Django 4.2.13 on 2024-07-26 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games_and_exercises', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizquestion',
            name='correct_choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='correct_for', to='games_and_exercises.choice'),
        ),
    ]
