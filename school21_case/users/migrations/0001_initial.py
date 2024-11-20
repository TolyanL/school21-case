# Generated by Django 5.1.2 on 2024-11-20 13:00

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=32, unique=True, verbose_name='Никнейм')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Описание профиля')),
                ('name', models.CharField(blank=True, null=True, verbose_name='Имя')),
                ('surname', models.CharField(blank=True, null=True, verbose_name='Фамилия')),
                ('lastname', models.CharField(blank=True, null=True, verbose_name='Отчество')),
                ('age', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)], verbose_name='Возраст')),
                ('gender', models.CharField(blank=True, choices=[('мужской', 'Мужской'), ('женский', 'Женский')], null=True, verbose_name='Пол')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='Аватар')),
                ('nickname_tg', models.CharField(blank=True, null=True, verbose_name='Никнейм в Telegram')),
                ('nickname_ds', models.CharField(blank=True, null=True, verbose_name='Никнейм в Discord')),
                ('study_at', models.CharField(blank=True, null=True, verbose_name='Учебное заведение')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('friends', models.ManyToManyField(blank=True, related_name='friends', to='users.profile', verbose_name='Друзья')),
                ('groups', models.ManyToManyField(blank=True, related_name='groups', to='groups.group', verbose_name='Группы')),
                ('interests', models.ManyToManyField(blank=True, related_name='related_profiles', to='groups.interest', verbose_name='Интересы')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
