from random import randint

from django.core.management.base import BaseCommand

from faker import Faker

from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Create random teachers'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, nargs='?', default=10)

    def handle(self, *args, **kwargs):
        fa = Faker()
        count = kwargs['count']
        for i in range(count):
            tch = Teacher(
                first_name=fa.first_name(),
                last_name=fa.last_name(),
                num_of_courses=randint(1, 5),
                employment_date=fa.date_between_dates(date_start='-10y', date_end='-1y')
            )

            tch.save()
