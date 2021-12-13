import datetime

from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    num_of_courses = models.IntegerField()
    employment_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.num_of_courses} courses)'
