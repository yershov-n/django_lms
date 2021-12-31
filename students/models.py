import datetime
import random

from dateutil.relativedelta import relativedelta

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

# from core.validators import adult_validator
from core.models import Person
from core.validators import AdultValidator

from .validators import unique_number_validator

from groups.models import Group


class Students(Person):
    phone_number = models.CharField(
        max_length=20,
        default='',
        validators=[
            MinLengthValidator(7),
            unique_number_validator
        ]
    )
    enroll_date = models.DateField(default=datetime.date.today)
    graduate_date = models.DateField(default=datetime.date.today)
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        related_name='students'
    )

    @classmethod
    def _generate(cls):
        student = super()._generate()
        student.phone_number = random.randint(1000000, 9999999)
        student.save()
