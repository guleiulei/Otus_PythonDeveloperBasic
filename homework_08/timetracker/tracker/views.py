from django.shortcuts import render
from django.views.generic import ListView, DetailView
from tracker.models import Task, Epic


def main_page(request):
    task = Task.objects.all()
    epic = Epic.objects.all()
    context = {
        'task': task,
        'epic': epic,
    }
    return render(request, 'tracker/index.html', context=context)


class TaskListView(ListView):
    model = Task


class EpicListView(ListView):
    model = Epic


class AnimalDetailView(DetailView):
    model = Task
