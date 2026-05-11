from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

class UsersListView(ListView):
    model = User
    template_name = 'users_list.html'
    context_object_name = 'users'

class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'user_create.html'
    success_url = reverse_lazy('login')
    success_message = 'Пользователь успешно зарегистрирован'

class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username']
    template_name = 'user_update.html'
    success_url = reverse_lazy('users_list')
    success_message = 'Пользователь успешно изменен'

class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_delete.html'
    success_url = reverse_lazy('users_list')
    success_message = 'Пользователь успешно удален'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
