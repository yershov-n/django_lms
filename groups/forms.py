from django import forms
from django.forms import ChoiceField
from django.forms import ModelForm

from django_filters import FilterSet

from .models import Group


class GroupBaseForm(ModelForm):
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


class GroupUpdateForm(GroupBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['headman_field'] = ChoiceField(
            choices=[(st.id, str(st)) for st in self.instance.students.all()],
            label='Headman',
            required=False
        )

    class Meta(GroupBaseForm.Meta):
        # fields = '__all__'
        exclude = ['start_date', 'headman']


class GroupCreateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        exclude = ['start_date', 'headman']


class GroupsFilter(FilterSet):
    class Meta:
        model = Group
        fields = {
            'group_size': ['lt', 'gt'],
            'group_name': ['exact', 'icontains'],
            'course': ['exact']
        }
