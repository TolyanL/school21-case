# Generated by Django 5.1.2 on 2024-11-01 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='logo',
        ),
        migrations.AddField(
            model_name='group',
            name='icon',
            field=models.ImageField(null=True, upload_to='group_icons/'),
        ),
    ]
