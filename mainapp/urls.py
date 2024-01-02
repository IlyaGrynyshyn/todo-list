from django.urls import path, include
from mainapp.views import TodoListView

urlpatterns = [
    path("", TodoListView.as_view(), name="home")
]