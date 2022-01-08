import datetime
import random

from core.models import Person

from django.core.validators import MinLengthValidator
from django.db import models

from groups.models import Group

from .validators import unique_number_validator


class Teacher(Person):
    num_of_courses = models.IntegerField(
        null=True
    )
    employment_date = models.DateField(default=datetime.date.today)
    phone_number = models.CharField(
        max_length=20,
        default='',
        validators=[
            MinLengthValidator(7),
            unique_number_validator
        ]
    )
    salary = models.PositiveIntegerField(default=1500)
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        related_name='teachers'
    )

    @classmethod
    def _generate(cls):
        teacher = super()._generate()
        teacher.salary = random.randint(10000, 99999)
        teacher.save()
