import datetime

from django.core.validators import MinLengthValidator
from django.db import models

from .validators import unique_number_validator

from groups.models import Group


class Teacher(models.Model):
    first_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)]
    )
    last_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)]
    )
    num_of_courses = models.IntegerField()
    employment_date = models.DateField(default=datetime.date.today)
    phone_number = models.CharField(
        max_length=20,
        default='',
        validators=[
            MinLengthValidator(7),
            unique_number_validator
        ]
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        related_name='teachers'
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.num_of_courses} courses) - {self.phone_number}'
