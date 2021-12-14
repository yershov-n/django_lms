import datetime

from django.core.validators import MinLengthValidator
from django.db import models

from .validators import unique_number_validator


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

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.num_of_courses} courses)'
