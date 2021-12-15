from django.urls import path

from .views import create_group
from .views import delete_group
from .views import get_groups
from .views import update_group

app_name = 'groups'

urlpatterns = [
    path('', get_groups, name='list'),
    path('create/', create_group, name='create'),
    path('update/<int:pk>/', update_group, name='update'),
    path('delete/<int:pk>/', delete_group, name='delete'),
]
