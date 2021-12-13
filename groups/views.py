from django.http import HttpResponse
from django.shortcuts import render  # noqa

from webargs import fields
from webargs.djangoparser import use_args

from .models import Group
from .utils import format_records


@use_args(
    {
        'group_name': fields.Str(required=False),
        'course': fields.Str(required=False),
        'group_size': fields.Int(required=False),
    },
    location='query'
)
def get_groups(requests, args):
    groups = Group.objects.all()

    for key, value in args.items():
        if value:
            groups = groups.filter(**{key: value})

    html_form = """
        <form method="get">
            <label for="fname">Group name:</label>
            <input type="text" id="fname" name="group_name"></br><br>

            <label for="lname">Course:</label>
            <input type="text" id="lname" name="course"></br><br>

            <label for="age">Group size:</label>
            <input type="number" name="group_size"></br><br>

            <input type="submit" value="Submit">
        </form>
        """

    records = format_records(groups)

    response = html_form + records

    return HttpResponse(response)
