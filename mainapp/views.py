from django.shortcuts import render
from django.views.generic import ListView

from mainapp.models import Task


class TodoListView(ListView):
    model = Task
    context_object_name = 'tasks'
    ordering = ["-is_done", "-created"]
    template_name = 'mainapp/index.html'
