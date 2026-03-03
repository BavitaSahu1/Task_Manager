from django.db import models



class Task(models.Model):

    STATUS_CHOICES = (('Pending', 'Pending'), ('Completed', 'Completed'),)

    task_description = models.TextField(null=False, blank=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=False, blank=False)

    def __str__(self):
        task_info = f"Task {self.id} - {self.status}"
        return task_info