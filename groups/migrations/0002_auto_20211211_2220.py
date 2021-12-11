# Generated by Django 3.2.9 on 2021-12-11 22:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='course',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]
