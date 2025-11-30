from django import forms
from .models import Professor, Disciplinas, Tempo, Aula, Turma, DiaSemana, Semestre, Predio, Sala

class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                # CheckboxSelectMultiple renders multiple inputs, don't apply form-control
                pass
            else:
                field.widget.attrs['class'] = 'form-control'

class ProfessorForm(BootstrapModelForm):
    class Meta:
        model = Professor
        fields = '__all__'
        widgets = {
            'dias_proibidos': forms.CheckboxSelectMultiple,
            'cor': forms.TextInput(attrs={'type': 'color'}),
        }

class DisciplinasForm(BootstrapModelForm):
    class Meta:
        model = Disciplinas
        fields = '__all__'
        widgets = {
            'cor': forms.TextInput(attrs={'type': 'color'}),
        }

class TempoForm(BootstrapModelForm):
    class Meta:
        model = Tempo
        fields = '__all__'
        widgets = {
            'inicio': forms.TimeInput(attrs={'type': 'time'}),
            'fim': forms.TimeInput(attrs={'type': 'time'}),
        }

class AulaForm(BootstrapModelForm):
    class Meta:
        model = Aula
        fields = '__all__'
        widgets = {
            'horarios': forms.CheckboxSelectMultiple,
        }

class TurmaForm(BootstrapModelForm):
    class Meta:
        model = Turma
        fields = '__all__'
        widgets = {
            'dias': forms.CheckboxSelectMultiple,
            'cor': forms.TextInput(attrs={'type': 'color'}),
        }

class DiaSemanaForm(BootstrapModelForm):
    class Meta:
        model = DiaSemana
        fields = '__all__'
        widgets = {
            'tempos': forms.CheckboxSelectMultiple,
        }

class SemestreForm(BootstrapModelForm):
    class Meta:
        model = Semestre
        fields = '__all__'
        widgets = {
            'turmas': forms.CheckboxSelectMultiple,
        }

class PredioForm(BootstrapModelForm):
    class Meta:
        model = Predio
        fields = '__all__'

class SalaForm(BootstrapModelForm):
    class Meta:
        model = Sala
        fields = '__all__'
