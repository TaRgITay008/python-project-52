from django.contrib import admin
from django.urls import path, include
from task_manager import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', include('users.urls')),
    path('statuses/', include('statuses.urls')),   # <-- добавить
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
