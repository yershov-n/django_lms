from django.urls import path

# from .views import create_student
# from .views import delete_student
# from .views import get_students
# from .views import update_student

# from .views import UpdateStudentView
from .views import StudentCreateView
from .views import StudentDeleteView
from .views import StudentUpdateView
from .views import StudentsListView
from .views import generate_students

app_name = 'students'

urlpatterns = [
    path('', StudentsListView.as_view(), name='list'),                               # R
    path('generate/', generate_students, name='generate'),
    path('create/', StudentCreateView.as_view(), name='create'),                    # C
    # path('update/<int:pk>/', update_student, name='update'),           # U
    # path('update/<int:pk>/', UpdateStudentView.update_student, name='update'),  # U
    path('update/<int:ppk>/', StudentUpdateView.as_view(), name='update'),  # U
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete'),           # D
]
