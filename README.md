# Task_Manager --------
This is a simple Task Manager web application built using Python & Django.

In this project, users can add tasks with a description and status (Pending or Completed) and view all saved tasks in a table format.


# Features ----------

* Add new task using a form

* Required field validation

* Status choice field (Pending / Completed)

* View all saved tasks

* Auto-generated Task ID

* Data stored in MySQL database



# Tech Stack Used -------

Python

Django

HTML/CSS

MySQL database



# Project Functionality -------

* Created a Django project and a new app task_manager.

* Created a Task model with:

    task_description (TextField, required)

    status (ChoiceField: Pending / Completed)

* Created a ModelForm to handle form input.

* On form submission (POST request), data is saved to the database.

* On page load (GET request), all tasks are fetched using:

    Task.objects.all()

* All saved tasks are displayed in a table using Django template loop.



# How to Run This Project -------

    python manage.py runserver

    Open in browser:
        http://127.0.0.1:8000/

# Validation -------

* Task description is required.

* Status is required.

* Django ModelForm handles validation automatically.




# TASK DESCRIPTION -------
Create a new Django project and a new app (for example, task_manager).
Add the app to INSTALLED_APPS in settings.py.
Create a Task model with these fields:
task_id (auto generated primary key)
task_description (required text field)
status (required choice field: Pending, Completed)
Run migrations to create the database table.
Create a form (Django Form or ModelForm) to accept task_description and status.
Create a view that:
shows the form
saves the task on form submit (POST)
fetches all saved tasks to display (GET)
Create a template page that:
shows the input form at the top
shows a table below with columns: Task ID, Task Description, Status
Configure URLs to load this page (for example, /tasks/).
Make sure basic validation works (description and status should be required).
Push the project to GitHub and include a README with setup and run instructions.



Bavita Sahu
Python Developer