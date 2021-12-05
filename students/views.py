from django.http import HttpResponse
from django.shortcuts import render  # noqa

from faker import Faker

from students.models import Students

from webargs import fields
from webargs.djangoparser import use_kwargs


def index(request):
    return HttpResponse('<h1>Hello from Django!</h1>')


@use_kwargs(
    {
        'count': fields.Int(
            required=False,
            missing=10
        )
    },
    location='query'
)
def generate_students(request, count):
    fa = Faker()
    for i in range(count):
        st = Students(
            first_name=fa.first_name(),
            last_name=fa.last_name(),
            age=fa.pyint(1, 100),
            birthday=fa.date_between_dates(date_start='-45y', date_end='-5y')
        )

        st.save()

    return HttpResponse(f'<h1>{count} students were added</h1>')
