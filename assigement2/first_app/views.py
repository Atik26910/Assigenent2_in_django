from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import TaskModel


# Create your views here.
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_taks")

    else:
        form = TaskForm()
    return render(request, "./add_task.html", {"form": form})


def show_taks(request):
    tasks = TaskModel.objects.filter(is_completed=False)
    return render(request, "./show_task.html", {"tasks": tasks})


def edit_task(request, task_id):
    task = get_object_or_404(TaskModel, pk=task_id)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("show_taks")
    else:
        form = TaskForm(instance=task)
    return render(request, "./edit_task.html", {"form": form, "task": task})


def delete_task(request, task_id):
    task = get_object_or_404(TaskModel, pk=task_id)
    task.delete()
    return redirect("show_taks")


def complete_task(request, task_id):
    task = get_object_or_404(TaskModel, pk=task_id)
    task.is_completed = True
    task.save()
    return redirect("show_taks")


def completed_tasks(request):
    completed_tasks = TaskModel.objects.filter(is_completed=True)
    return render(request, './completed_task.html', {'completed_tasks': completed_tasks})
