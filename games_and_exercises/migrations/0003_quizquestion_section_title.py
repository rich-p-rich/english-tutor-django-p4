# Generated by Django 4.2.13 on 2024-07-25 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_and_exercises', '0002_quizquestion_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizquestion',
            name='section_title',
            field=models.CharField(default='TBC', max_length=255),
        ),
    ]