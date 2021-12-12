from django import forms

from .models import Teacher


class TeacherCreateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'num_of_courses',
            'employment_date',
            'phone_number'
        ]

        widgets = {
            'employment_date': forms.DateInput(attrs={'type': 'date'})
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