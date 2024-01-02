from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from mainapp.models import Task


class TodoListView(ListView):
    model = Task
    context_object_name = 'tasks'
    ordering = ["-is_done", "-created"]
    template_name = 'mainapp/index.html'


class TaskCrateView(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("home")


class TaskUpdateView(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("home")
