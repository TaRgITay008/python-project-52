import django_filters
from django import forms
from .models import Task
from statuses.models import Status
from labels.models import Label
from django.contrib.auth.models import User

class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label='Статус'
    )
    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        label='Исполнитель'
    )
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label='Метка'
    )
    only_self_tasks = django_filters.BooleanFilter(
        method='filter_only_self_tasks',
        label='Только свои задачи',
        widget=forms.CheckboxInput
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']

    def filter_only_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
