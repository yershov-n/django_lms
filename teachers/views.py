from django.http import HttpResponse
from django.shortcuts import render  # noqa

from webargs import fields
from webargs.djangoparser import use_args

from .models import Teacher
from .utils import format_records


@use_args(
    {
        'first_name': fields.Str(required=False),
        'last_name': fields.Str(required=False),
        'num_of_courses': fields.Int(required=False),
    },
    location='query'
)
def get_teachers(requests, args):
    teachers = Teacher.objects.all()

    for key, value in args.items():
        if value:
            teachers = teachers.filter(**{key: value})

    html_form = """
        <form method="get">
            <label for="fname">First name:</label>
            <input type="text" id="fname" name="first_name"></br><br>

            <label for="lname">Last name:</label>
            <input type="text" id="lname" name="last_name"></br><br>

            <label for="age">Number of courses:</label>
            <input type="number" name="num_of_courses"></br><br>

            <input type="submit" value="Submit">
        </form>
        """

    records = format_records(teachers)

    response = html_form + records

    return HttpResponse(response)
