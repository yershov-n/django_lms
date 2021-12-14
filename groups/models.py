import datetime

from django.core.validators import MinLengthValidator
from django.db import models


class Group(models.Model):
    group_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)]
    )
    course = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)]
    )
    group_size = models.IntegerField()
    start_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.group_name} ({self.course}) - {self.group_size} students'
