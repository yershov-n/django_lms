from django import forms

from django_filters import FilterSet

from .models import Course


class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Course

        fields = '__all__'


class CoursesFilter(FilterSet):
    class Meta:
        model = Course
        fields = {
            'name': ['exact', 'icontains'],
            'price': ['lt', 'gt'],
        }
