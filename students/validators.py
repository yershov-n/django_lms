import datetime

from django.core.exceptions import ValidationError

ADULT_AGE_LIMIT = 18


def adult_validator(birthday):
    age = datetime.date.today().year - birthday.year
    if age < ADULT_AGE_LIMIT:
        raise ValidationError('Age should be greater than 18 y.o.')


def unique_number_validator(phone_number):
    from .models import Students
    if Students.objects.filter(phone_number=phone_number).exists():
        raise ValidationError('Phone number already exist')
