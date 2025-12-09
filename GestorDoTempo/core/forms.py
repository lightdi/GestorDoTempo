from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        # Verifica se o email termina com @ifpb.edu.br
        if not user.email.endswith('@ifpb.edu.br'):
            raise ValidationError(
                "Acesso permitido apenas para e-mails do domínio @ifpb.edu.br",
                code='invalid_domain',
            )

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Obrigatório. Deve ser um e-mail @ifpb.edu.br')

    class Meta:
        model = User
        fields = ("username", "email")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not email.endswith('@ifpb.edu.br'):
            raise ValidationError("O e-mail deve terminar com @ifpb.edu.br")
        return email

class UserUpdateForm(forms.ModelForm):
    is_staff = forms.BooleanField(label="Administrador", required=False)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'is_staff']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not email.endswith('@ifpb.edu.br'):
            raise ValidationError("O e-mail deve terminar com @ifpb.edu.br")
        return email
