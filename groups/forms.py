from django import forms
from django_filters import FilterSet

from .models import Group


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        # fields = [
        #     'group_name',
        #     'course',
        #     'group_size',
        #     'start_date'
        # ]

        fields = '__all__'

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'})
        }


class GroupsFilter(FilterSet):
    class Meta:
        model = Group
        fields = {
            'group_size': ['lt', 'gt'],
            'group_name': ['exact', 'icontains'],
            'course': ['exact']
        }