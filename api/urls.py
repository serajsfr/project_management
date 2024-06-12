from django.urls import path
from .views import TaskListCreateView, TaskDetailView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]