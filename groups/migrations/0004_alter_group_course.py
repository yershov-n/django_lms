# Generated by Django 3.2.9 on 2021-12-31 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('groups', '0003_group_teachers_gr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='course',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course', to='courses.course'),
        ),
    ]
