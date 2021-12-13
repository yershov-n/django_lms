import datetime

from django.core.exceptions import ValidationError

ADULT_AGE_LIMIT = 18


def adult_validator(birthday, age_limit=18):
    age = datetime.date.today().year - birthday.year
    if age < age_limit:
        raise ValidationError(f'Age should be greater than {age_limit} y.o.')


def unique_number_validator(phone_number):
    from .models import Students
    if Students.objects.filter(phone_number=phone_number).exists():
        raise ValidationError('Phone number already exist')


class AdultValidator:
    def __init__(self, age_limit):
        self.age_limit = age_limit

    # def __call__(self, birthday):
    def __call__(self, *args, **kwargs):
        # adult_validator(args[0], self.age_limit)
        age = datetime.date.today().year - args[0].year
        if age < self.age_limit:
            raise ValidationError(f'Age should be greater than {self.age_limit} y.o.')
