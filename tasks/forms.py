from django import forms
from .models import Task
from statuses.models import Status
from django.contrib.auth.models import User
from labels.models import Label

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].queryset = Status.objects.all()
        self.fields['executor'].queryset = User.objects.all()
        self.fields['labels'].queryset = Label.objects.all()
        self.fields['executor'].required = False
        self.fields['labels'].required = False
