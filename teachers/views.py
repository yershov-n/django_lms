from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import TeacherCreateForm, TeacherUpdateForm
from .forms import TeachersFilter
from .models import Teacher


class TeachersListView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'

    def get_queryset(self):
        filter_teachers = TeachersFilter(
            data=self.request.GET,
            queryset=self.model.objects.all()
        )

        return filter_teachers


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/delete.html'


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = TeacherUpdateForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'


class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    form_class = TeacherCreateForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/create.html'
