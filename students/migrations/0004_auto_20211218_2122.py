# Generated by Django 3.2.9 on 2021-12-18 21:22

import core.validators
import datetime
import django.core.validators
from django.db import migrations, models
import students.validators


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20211211_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='enroll_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='students',
            name='graduate_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='students',
            name='birthday',
            field=models.DateField(default=datetime.date.today, validators=[core.validators.AdultValidator(20)]),
        ),
        migrations.AlterField(
            model_name='students',
            name='phone_number',
            field=models.CharField(default='', max_length=20, validators=[django.core.validators.MinLengthValidator(7), students.validators.unique_number_validator]),
        ),
    ]