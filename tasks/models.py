from django.db import models
from django.contrib.auth.models import User
from statuses.models import Status

class Task(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author_tasks')
    executor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='executor_tasks', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
