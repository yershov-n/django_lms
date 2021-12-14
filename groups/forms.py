from django import forms

from .models import Group


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'group_name',
            'course',
            'group_size',
            'start_date'
        ]

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'})
        }
