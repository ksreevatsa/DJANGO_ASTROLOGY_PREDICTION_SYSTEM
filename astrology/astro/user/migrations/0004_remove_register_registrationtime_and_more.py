# Generated by Django 4.2.6 on 2023-10-13 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_register_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='registrationtime',
        ),
        migrations.AlterField(
            model_name='register',
            name='gender',
            field=models.CharField(choices=[('Prefer not to say', 'Prefer not to say'), ('Male', 'Male'), ('Female', 'Female')], max_length=100),
        ),
    ]