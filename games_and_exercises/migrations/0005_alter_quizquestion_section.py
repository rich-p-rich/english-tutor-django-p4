# Generated by Django 4.2.13 on 2024-07-25 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games_and_exercises', '0004_section_remove_quizquestion_section_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizquestion',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='games_and_exercises.section'),
        ),
    ]
