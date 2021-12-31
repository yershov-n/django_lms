import datetime

from django.core.validators import MinLengthValidator
from django.db import models

# from students.models import Students
# from teachers.models import Teacher


class Group(models.Model):
    group_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)]
    )
    course = models.OneToOneField(
        'courses.Course',
        on_delete=models.SET_NULL,
        null=True,
        related_name='course'
    )
    group_size = models.IntegerField()
    start_date = models.DateField(default=datetime.date.today)

    headman = models.OneToOneField(
        'students.Students',
        on_delete=models.SET_NULL,
        null=True,
        related_name='headman_group'
    )

    teachers_gr = models.ManyToManyField(
        to='teachers.Teacher',
        related_name='groups'
    )

    def __str__(self):
        return self.group_name
