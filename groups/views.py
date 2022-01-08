from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from students.models import Students

from webargs import fields  # noqa
from webargs.djangoparser import use_args  # noqa

from .forms import GroupCreateForm, GroupUpdateForm
from .forms import GroupsFilter
from .models import Group


# @use_args(
#     {
#         'group_name': fields.Str(required=False),
#         'course': fields.Str(required=False),
#         'group_size': fields.Int(required=False),
#     },
#     location='query'
# )
# def get_groups(request, args):
#     groups = Group.objects.all().select_related('course')
#
#     filter_groups = GroupsFilter(data=request.GET, queryset=groups)
#
#     return render(
#         request=request,
#         template_name='groups/list.html',
#         context={
#             'groups': groups,
#             'filter_groups': filter_groups
#         }
#     )


def create_group(request):

    if request.method == 'GET':
        form = GroupUpdateForm()
    elif request.method == 'POST':
        form = GroupUpdateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/create.html',
        context={'form': form}
    )


# def update_group(request, pk):
#     group = get_object_or_404(Group, id=pk)
#
#     if request.method == 'GET':
#         form = GroupUpdateForm(instance=group)
#     elif request.method == 'POST':
#         form = GroupUpdateForm(data=request.POST, instance=group)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('groups:list'))
#
#     return render(
#         request=request,
#         template_name='groups/update.html',
#         context={
#             'form': form,
#             'group': group,
#             'students': group.students.prefetch_related('headman_group'),
#             'teachers': group.teachers_gr.prefetch_related('group'),
#         }
#     )


def delete_group(request, pk):
    group = get_object_or_404(Group, id=pk)
    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/delete.html', {'group': group})


class GroupListView(ListView):
    model = Group
    template_name = 'groups/list.html'

    def get_queryset(self):
        filter_groups = GroupsFilter(
            data=self.request.GET,
            queryset=self.model.objects.all().select_related('course'))

        return filter_groups


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupCreateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/create.html'


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupUpdateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = self.get_object().students.prefetch_related('headman_group')
        context['teachers'] = self.get_object().teachers_gr.prefetch_related('group')

        return context

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['headman_field'] = self.object.headman.id
        except AttributeError as ex:  # noqa
            pass

        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        pk = form.cleaned_data['headman_field']
        if pk:
            form.instance.headman = Students.objects.get(id=form.cleaned_data['headman_field'])
        form.instance.save()

        return response


class GroupDeleteView(DeleteView):
    model = Group
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/delete.html'
