# Generated by Django 3.2.9 on 2021-12-18 21:22

import django.core.validators
from django.db import migrations, models
import teachers.validators


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20211211_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(default='', max_length=20, validators=[django.core.validators.MinLengthValidator(7), teachers.validators.unique_number_validator]),
        ),
    ]