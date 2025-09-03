from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("manage/", views.task_management, name='task_management'),
    path("tasks/", views.view_tasks, name='view_tasks'),
]