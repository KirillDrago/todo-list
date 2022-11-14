from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from app.forms import TaskForm
from app.models import Task, Tag


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("app:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("app:tag-list")
    template_name = "app/tag_confirm_delete.html"


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all()


class TaskCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("app:task-list")
    form_class = TaskForm


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("app:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("app:task-list")


def task_status(request, pk):
    task = Task.objects.get(pk=pk)
    if task.status:
        task.status = False
    else:
        task.status = True
    task.save()
    return redirect("app:task-list")
