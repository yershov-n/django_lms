from django.urls import path

from .views import create_student
from .views import delete_student
from .views import generate_students
# from .views import get_students
# from .views import update_student

# from .views import UpdateStudentView
from .views import StudentUpdateView
from .views import StudentsListView

app_name = 'students'

urlpatterns = [
    path('', StudentsListView.as_view(), name='list'),                               # R
    path('generate/', generate_students, name='generate'),
    path('create/', create_student, name='create'),                    # C
    # path('update/<int:pk>/', update_student, name='update'),           # U
    # path('update/<int:pk>/', UpdateStudentView.update_student, name='update'),  # U
    path('update/<int:ppk>/', StudentUpdateView.as_view(), name='update'),  # U
    path('delete/<int:pk>/', delete_student, name='delete'),           # D
]
