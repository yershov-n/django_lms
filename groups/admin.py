from django.contrib import admin  # noqa

from .models import Group

from students.models import Students


class StudentsInlineTable(admin.TabularInline):
    model = Students
    fields = [
        'first_name',
        'last_name',
        'birthday',
        'phone_number',
    ]

    extra = 0
    # readonly_fields = fields
    # show_change_link = True


class GroupAdmin(admin.ModelAdmin):
    list_display = [
        'group_name',
        'start_date',
        'headman',
    ]

    fields = [
        'group_name',
        'start_date',
        'headman',
        'teachers_gr',
    ]

    inlines = [StudentsInlineTable,]


admin.site.register(Group, GroupAdmin)
