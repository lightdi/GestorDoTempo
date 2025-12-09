from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    DashboardView, CustomLoginView, SignUpView, 
    UserListView, UserCreateView, UserUpdateView, UserDeleteView
)

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    
    # User Management
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/add/', UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/edit/', UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
]
