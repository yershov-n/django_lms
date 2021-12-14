from django.core.exceptions import ValidationError


def unique_number_validator(phone_number):
    from .models import Teacher
    if Teacher.objects.filter(phone_number=phone_number).exists():
        raise ValidationError('Phone number already exist')
