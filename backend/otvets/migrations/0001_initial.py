# Generated by Django 5.1.1 on 2024-10-15 13:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0002_alter_questions_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Otvets',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('discription', models.TextField(verbose_name='Ответ')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('rating', models.IntegerField(default=0, verbose_name='Рейтинг')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.questions', verbose_name='Вопрос')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
                'db_table': 'otvet',
            },
        ),
    ]
