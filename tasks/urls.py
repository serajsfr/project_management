from django.urls import path
from .views import task_list, task_detail, task_create, task_update, task_delete


urlpatterns = [
    path('', task_list, name='task-list-ui'),
    path('tasks/<int:pk>/', task_detail, name='task-detail-ui'),
    path('tasks/create/', task_create, name='task-create-ui'),
    path('tasks/<int:pk>/edit', task_update, name='task-update-ui'),
    path('tasks/<int:pk>/delete/', task_delete, name='task-delete-ui'),
]