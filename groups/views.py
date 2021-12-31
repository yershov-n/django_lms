from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from webargs import fields
from webargs.djangoparser import use_args

from .forms import GroupCreateForm
from .forms import GroupsFilter
from .models import Group


@use_args(
    {
        'group_name': fields.Str(required=False),
        'course': fields.Str(required=False),
        'group_size': fields.Int(required=False),
    },
    location='query'
)
def get_groups(request, args):
    groups = Group.objects.all().select_related('course')

    filter_groups = GroupsFilter(data=request.GET, queryset=groups)

    return render(
        request=request,
        template_name='groups/list.html',
        context={
            'groups': groups,
            'filter_groups': filter_groups
        }
    )


def create_group(request):

    if request.method == 'GET':
        form = GroupCreateForm()
    elif request.method == 'POST':
        form = GroupCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/create.html',
        context={'form': form}
    )


def update_group(request, pk):
    group = get_object_or_404(Group, id=pk)
    if request.method == 'GET':
        form = GroupCreateForm(instance=group)
    elif request.method == 'POST':
        form = GroupCreateForm(data=request.POST, instance=group)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/update.html',
        context={
            'form': form,
            'group': group,
            'students': group.students.prefetch_related('headman_group'),
            'teachers': group.teachers_gr.prefetch_related('group'),
        }
    )


def delete_group(request, pk):
    group = get_object_or_404(Group, id=pk)
    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/delete.html', {'group': group})
