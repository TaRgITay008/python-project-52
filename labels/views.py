from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Label

class LabelsListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'labels_list.html'
    context_object_name = 'labels'

class LabelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Label
    fields = ['name']
    template_name = 'label_create.html'
    success_url = reverse_lazy('labels_list')
    success_message = 'Метка успешно создана'

class LabelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    fields = ['name']
    template_name = 'label_update.html'
    success_url = reverse_lazy('labels_list')
    success_message = 'Метка успешно изменена'

class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'label_delete.html'
    success_url = reverse_lazy('labels_list')
    success_message = 'Метка успешно удалена'

    def delete(self, request, *args, **kwargs):
        messages.success(request, self.success_message)
        return super().delete(request, *args, **kwargs)
