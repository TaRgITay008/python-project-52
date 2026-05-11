from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users import views

urlpatterns = [
    path('', views.UsersListView.as_view(), name='users_list'),
    path('create/', views.UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
