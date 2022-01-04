from django.core.validators import MinLengthValidator
from django.db import models


class Course(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)]
    )
    max_group_size = models.IntegerField()
    price = models.IntegerField()
    num_of_lessons = models.IntegerField()

    def __str__(self):
        return f'{self.name}'
