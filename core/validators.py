import datetime

from django.core.exceptions import ValidationError

ADULT_AGE_LIMIT = 18


def adult_validator(birthday, age_limit=18):
    age = datetime.date.today().year - birthday.year
    if age < age_limit:
        raise ValidationError(f'Age should be greater than {age_limit} y.o.')


class AdultValidator:
    def __init__(self, age_limit):
        self.age_limit = age_limit

    # def __call__(self, birthday):
    def __call__(self, *args, **kwargs):
        # adult_validator(args[0], self.age_limit)
        age = datetime.date.today().year - args[0].year
        if age < self.age_limit:
            raise ValidationError(f'Age should be greater than {self.age_limit} y.o.')
