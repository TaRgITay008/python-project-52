from django.db import models
from django.core.exceptions import ValidationError

class Label(models.Model):
    name = models.CharField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        if self.tasks.exists():
            raise ValidationError("Невозможно удалить метку, она связана с задачей")
        super().delete(*args, **kwargs)
