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


############### TASK DESCRIPTION ###############
# Create a new Django project and a new app (for example, task_manager).
# Add the app to INSTALLED_APPS in settings.py.
# Create a Task model with these fields:
# task_id (auto generated primary key)
# task_description (required text field)
# status (required choice field: Pending, Completed)
# Run migrations to create the database table.
# Create a form (Django Form or ModelForm) to accept task_description and status.
# Create a view that:
# shows the form
# saves the task on form submit (POST)
# fetches all saved tasks to display (GET)
# Create a template page that:
# shows the input form at the top
# shows a table below with columns: Task ID, Task Description, Status
# Configure URLs to load this page (for example, /tasks/).
# Make sure basic validation works (description and status should be required).
# Push the project to GitHub and include a README with setup and run instructions.