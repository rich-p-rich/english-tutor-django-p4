# Generated by Django 4.2.13 on 2024-08-02 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0001_initial'),
        ('appointments', '0005_remove_appointment_email_remove_appointment_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='user_profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_accounts.userprofile'),
            preserve_default=False,
        ),
    ]
