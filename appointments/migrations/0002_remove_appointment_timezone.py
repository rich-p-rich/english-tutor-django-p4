# Generated by Django 4.2.13 on 2024-07-04 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='timezone',
        ),
    ]