import datetime
import random

from core.models import Person

from dateutil.relativedelta import relativedelta  # noqa

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker  # noqa

# from core.validators import adult_validator
from core.validators import AdultValidator  # noqa

from groups.models import Group

from .validators import unique_number_validator


class Students(Person):
    phone_number = models.CharField(
        max_length=20,
        default='',
        # validators=[
        #     MinLengthValidator(7),
        #     unique_number_validator
        # ]
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
