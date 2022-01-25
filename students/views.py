from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect  # noqa
from django.shortcuts import get_object_or_404  # noqa
from django.shortcuts import render  # noqa
from django.urls import reverse  # noqa
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt  # noqa
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from faker import Faker

from webargs import fields
from webargs.djangoparser import use_args  # noqa
from webargs.djangoparser import use_kwargs

from core.views import UpdateBaseView  # noqa

from .forms import StudentCreateForm, StudentUpdateForm
from .forms import StudentsFilter
from .models import Students
# from .utils import format_records  # noqa


@login_required
@use_kwargs(
    {
        'count': fields.Int(
            required=False,
            missing=10
        )
    },
    location='query'
)
def generate_students(request, count):
    fa = Faker()
    for i in range(count):
        st = Students(
            first_name=fa.first_name(),
            last_name=fa.last_name(),
            age=fa.pyint(1, 100),
            birthday=fa.date_between_dates(date_start='-45y', date_end='-5y')
        )

        st.save()

    return HttpResponse(f'<h1>{count} students were added</h1>')


# @use_args(
#     {
#         'first_name': fields.Str(required=False),
#         'last_name': fields.Str(required=False),
#         'age': fields.Int(required=False),
#     },
#     location='query'
# )
# def get_students(request, args):
#     students = Students.objects.all().select_related('group', 'headman_group')
#
#     # for key, value in args.items():
#     #     if value:
#     #         students = students.filter(**{key: value})
#
#     # html_form = """
#     #     <form method="get">
#     #         <label for="fname">First name:</label>
#     #         <input type="text" id="fname" name="first_name"></br><br>
#     #         <label for="lname">Last name:</label>
#     #         <input type="text" id="lname" name="last_name"></br><br>
#     #         <label for="age">Age:</label>
#     #         <input type="number" name="age"></br><br>
#     #         <input type="submit" value="Search">
#     #     </form>
#     #     """
#     #
#     # records = format_records(students)
#     #
#     # response = html_form + records
#
#     # return HttpResponse(response)
#
#     filter_students = StudentsFilter(data=request.GET, queryset=students)
#
#     return render(
#         request=request,
#         template_name='students/list.html',
#         context={
#             'students': students,
#             'filter_students': filter_students
#         }
#     )


# @csrf_exempt
# def create_student(request):
#
#     if request.method == 'GET':
#         form = StudentCreateForm()
#     elif request.method == 'POST':
#         form = StudentCreateForm(data=request.POST)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('students:list'))
#
#     # html_form = f"""
#     #         <form method="post">
#     #             {form.as_p()}
#     #
#     #             <input type="submit" value="Create">
#     #         </form>
#     #         """
#
#     # return HttpResponse(html_form)
#     return render(
#         request=request,
#         template_name='students/create.html',
#         context={'form': form}
#     )


# def update_student(request, pk):
#     student = get_object_or_404(Students, id=pk)
#
#     if request.method == 'GET':
#         form = StudentCreateForm(instance=student)
#     elif request.method == 'POST':
#         form = StudentCreateForm(data=request.POST, instance=student)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('students:list'))
#
#     return render(
#         request,
#         'students/update.html',
#         {
#             'form': form
#         }
#     )

# @login_required
# def delete_student(request, pk):
#     student = get_object_or_404(Students, id=pk)
#     if request.method == 'POST':
#         student.delete()
#         return HttpResponseRedirect(reverse('students:list'))
#
#     return render(request, 'students/delete.html', {'student': student})


# class UpdateStudentView(UpdateBaseView):
#     model = Students
#     form_class = StudentUpdateForm
#     success_url = 'students:list'
#     template_name = 'students/update.html'


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Students
    form_class = StudentUpdateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'

    pk_url_kwarg = 'ppk'


class StudentsListView(ListView):
    paginate_by = 10
    model = Students
    template_name = 'students/list.html'

    def get_filter(self):
        return StudentsFilter(
            data=self.request.GET,
            queryset=self.model.objects.all().select_related('group', 'headman_group')
        )

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = self.get_filter().form

        return context


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Students
    success_url = reverse_lazy('students:list')
    template_name = 'students/delete.html'


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Students
    form_class = StudentCreateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/create.html'
