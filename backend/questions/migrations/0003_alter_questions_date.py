# Generated by Django 5.1.1 on 2024-10-19 21:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_alter_questions_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 20, 1, 57, 36, 722055), verbose_name='Дата'),
        ),
    ]
