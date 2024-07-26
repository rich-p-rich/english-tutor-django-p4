# Generated by Django 4.2.13 on 2024-07-26 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games_and_exercises', '0006_alter_quizquestion_section'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizquestion',
            name='level',
        ),
        migrations.AddField(
            model_name='section',
            name='level',
            field=models.CharField(default='TBC', max_length=10),
        ),
        migrations.AlterField(
            model_name='quizquestion',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='games_and_exercises.section'),
        ),
    ]