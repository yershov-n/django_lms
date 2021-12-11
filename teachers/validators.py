from django.core.exceptions import ValidationError


def unique_number_validator(phone_number):
    from .models import Teacher
    if Teacher.objects.all().filter(phone_number=f'{phone_number}'):
        raise ValidationError('Phone number already exist')
