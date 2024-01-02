from django.urls import path, include
from mainapp.views import TodoListView, TaskCrateView

urlpatterns = [
    path("", TodoListView.as_view(), name="home"),
    path("create/", TaskCrateView.as_view(), name="create-tast")
]