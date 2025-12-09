from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm, CustomUserCreationForm

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'core/login.html'

from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'core/signup.html'

from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin
from .forms import UserUpdateForm

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class UserListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = User
    template_name = 'core/user_list.html'
    context_object_name = 'users'

class UserCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'core/user_form.html'
    success_url = reverse_lazy('user_list')

class UserUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'core/user_form.html'
    success_url = reverse_lazy('user_list')

class UserDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = User
    template_name = 'core/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')
