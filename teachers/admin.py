from django.contrib import admin  # noqa

from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'employment_date',
        'phone_number',
    ]

    fields = [
        ('first_name', 'last_name'),
        'employment_date',
        'phone_number',
        'salary',
    ]


admin.site.register(Teacher, TeacherAdmin)
