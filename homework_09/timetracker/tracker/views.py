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
    context_object_name = 'task-list'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['help_text'] = 'Тебе в помощь'
        return context


class EpicListView(ListView):
    model = Epic


class AnimalDetailView(DetailView):
    model = Task
