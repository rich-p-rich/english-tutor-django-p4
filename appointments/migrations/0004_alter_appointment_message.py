# Generated by Django 4.2.13 on 2024-08-01 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_appointment_surname_alter_appointment_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='message',
            field=models.TextField(default='Optional message', max_length=1000),
        ),
    ]
