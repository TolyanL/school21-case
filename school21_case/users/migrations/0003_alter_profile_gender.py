# Generated by Django 5.1.2 on 2024-10-31 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_age_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], null=True),
        ),
    ]