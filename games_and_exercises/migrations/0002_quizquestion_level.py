# Generated by Django 4.2.13 on 2024-07-24 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_and_exercises', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizquestion',
            name='level',
            field=models.CharField(default='TBC', max_length=10),
        ),
    ]
