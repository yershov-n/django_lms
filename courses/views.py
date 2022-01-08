from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from webargs import fields
from webargs.djangoparser import use_args

from .forms import CourseUpdateForm
from .forms import CoursesFilter
from .models import Course


@use_args(
    {
        'name': fields.Str(required=False),
        'max_group_size': fields.Int(required=False),
        'price': fields.Int(required=False),
        'num_of_lessons': fields.Int(required=False),
    },
    location='query'
)
def get_courses(request, args):
    courses = Course.objects.all()

    for key, value in args.items():
        if value:
            courses = courses.filter(**{key: value})

    filter_courses = CoursesFilter(data=request.GET, queryset=courses)

    return render(
        request=request,
        template_name='courses/list.html',
        context={
            'courses': courses,
            'filter_courses': filter_courses
        }
    )


def create_course(request):

    if request.method == 'GET':
        form = CourseUpdateForm()
    elif request.method == 'POST':
        form = CourseUpdateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))

    return render(
        request=request,
        template_name='courses/create.html',
        context={'form': form}
    )


def update_course(request, pk):
    course = get_object_or_404(Course, id=pk)
    if request.method == 'GET':
        form = CourseUpdateForm(instance=course)
    elif request.method == 'POST':
        form = CourseUpdateForm(data=request.POST, instance=course)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))

    return render(
        request=request,
        template_name='courses/update.html',
        context={
            'form': form
        }
    )


def delete_course(request, pk):
    course = get_object_or_404(Course, id=pk)
    if request.method == 'POST':
        course.delete()
        return HttpResponseRedirect(reverse('courses:list'))

    return render(request, 'courses/delete.html', {'course': course})
