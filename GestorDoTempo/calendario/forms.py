from django import forms
from .models import Event, TipoEventos

class TipoEventosForm(forms.ModelForm):
    class Meta:
        model = TipoEventos
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cor': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'integrado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'superior': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'tipo', 'curso', 'turma', 'data_inicio', 'data_fim', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'curso': forms.Select(attrs={'class': 'form-select'}),
            'turma': forms.Select(attrs={'class': 'form-select'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'data_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'data_fim': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
