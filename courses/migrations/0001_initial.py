# Generated by Django 3.2.9 on 2021-12-31 10:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('max_group_size', models.IntegerField()),
                ('price', models.IntegerField()),
                ('num_of_lessons', models.IntegerField()),
            ],
        ),
    ]