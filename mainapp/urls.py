from django.urls import path, include
from mainapp.views import TodoListView, TaskCrateView, TaskUpdateView

urlpatterns = [
    path("", TodoListView.as_view(), name="home"),
    path("create-task/", TaskCrateView.as_view(), name="create-task"),
    path("update-task", TaskUpdateView.as_view(), name="update-task")
]