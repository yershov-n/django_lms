from django import forms
from django.forms import ModelForm

from django_filters import FilterSet

from .models import Students


class StudentBaseForm(ModelForm):
    class Meta:
        model = Students
        fields = '__all__'

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    @staticmethod
    def normalize_name(value):
        return value.lower().capitalize()

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return self.normalize_name(first_name)

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return self.normalize_name(last_name)

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        clean_phone_number = ''
        for char in phone_number:
            if char.isdigit():
                clean_phone_number += char
        return clean_phone_number


class StudentCreateForm(StudentBaseForm):
    class Meta(StudentBaseForm.Meta):
        exclude = ['age']


class StudentUpdateForm(StudentBaseForm):
    class Meta(StudentBaseForm.Meta):
        exclude = ['age']


class StudentsFilter(FilterSet):
    class Meta:
        model = Students
        fields = {
            'age': ['lt', 'gt'],
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith']
        }
