from django.contrib import admin
from django.urls import path, include
from task_manager import views
from users import views as user_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', user_views.UsersListView.as_view(), name='users_list'),
    path('users/create/', user_views.UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', user_views.UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', user_views.UserDeleteView.as_view(), name='user_delete'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
