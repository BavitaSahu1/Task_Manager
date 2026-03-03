from django.shortcuts import render, redirect
from django.http import HttpResponse
from task_manager.forms import TaskForm
from task_manager.models import Task


def task_description(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_description')
        
    else:
        form = TaskForm()

    tasks = Task.objects.all()

    return render(request, 'task_description.html', {'form': form, 'tasks': tasks})
