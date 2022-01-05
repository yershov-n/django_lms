from django.urls import path

# from .views import create_group
# from .views import delete_group
# from .views import get_groups
# from .views import update_group

from .views import GroupCreateView
from .views import GroupListView
from .views import GroupUpdateView
from .views import GroupDeleteView

app_name = 'groups'

urlpatterns = [
    path('', GroupListView.as_view(), name='list'),
    path('create/', GroupCreateView.as_view(), name='create'),
    path('update/<int:pk>/', GroupUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', GroupDeleteView.as_view(), name='delete'),
]
