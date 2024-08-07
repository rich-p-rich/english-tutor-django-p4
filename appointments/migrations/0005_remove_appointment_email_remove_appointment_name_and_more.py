# Generated by Django 4.2.13 on 2024-08-02 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0001_initial'),
        ('appointments', '0004_alter_appointment_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='name',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='surname',
        ),
        migrations.AddField(
            model_name='appointment',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_accounts.userprofile'),
        ),
    ]
