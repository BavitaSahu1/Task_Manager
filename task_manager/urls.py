from django.contrib import admin
from django.urls import path
from task_manager import views

urlpatterns = [
    path('',views.task_description,name="task_description"),
]