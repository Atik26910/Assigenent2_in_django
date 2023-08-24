from django.db import models

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.CharField(max_length=500)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.taskTitle