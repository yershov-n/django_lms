from django.http import HttpResponseRedirect
from django.shortcuts import render

from webargs import fields
from webargs.djangoparser import use_args

from .forms import GroupCreateForm
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
    groups = Group.objects.all()

    for key, value in args.items():
        if value:
            groups = groups.filter(**{key: value})

    return render(
        request=request,
        template_name='groups/list.html',
        context={'groups': groups}
    )


def create_group(request):

    if request.method == 'GET':
        form = GroupCreateForm()
    elif request.method == 'POST':
        form = GroupCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')

    return render(
        request=request,
        template_name='groups/create.html',
        context={'form': form}
    )


def update_group(request, pk):
    group = Group.objects.get(id=pk)
    if request.method == 'GET':
        form = GroupCreateForm(instance=group)
    elif request.method == 'POST':
        form = GroupCreateForm(data=request.POST, instance=group)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')

    return render(
        request=request,
        template_name='groups/update.html',
        context={'form': form}
    )
