# Generated by Django 3.2.9 on 2022-01-30 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='phone_number',
            field=models.CharField(default='', max_length=20),
        ),
    ]
