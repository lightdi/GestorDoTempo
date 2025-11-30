from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Professor, Disciplinas, Tempo, Aula, Turma, DiaSemana, Semestre, Predio, Sala
from .forms import (
    ProfessorForm, DisciplinasForm, TempoForm, AulaForm, TurmaForm, 
    DiaSemanaForm, SemestreForm, PredioForm, SalaForm
)

@require_POST
def create_aula_ajax(request):
    try:
        professor_id = request.POST.get('professor')
        disciplina_id = request.POST.get('disciplina')
        sala_id = request.POST.get('sala')

        if not all([professor_id, disciplina_id, sala_id]):
            return JsonResponse({'error': 'Todos os campos são obrigatórios.'}, status=400)

        aula = Aula.objects.create(
            professor_id=professor_id,
            disciplina_id=disciplina_id,
            sala_id=sala_id
        )
        
        return JsonResponse({
            'id': aula.id,
            'text': str(aula)
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def get_aula_details_ajax(request, pk):
    try:
        aula = get_object_or_404(Aula, pk=pk)
        return JsonResponse({
            'id': aula.id,
            'professor_id': aula.professor.id,
            'disciplina_id': aula.disciplina.id,
            'sala_id': aula.sala.id
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@require_POST
def update_aula_ajax(request):
    try:
        aula_id = request.POST.get('id')
        professor_id = request.POST.get('professor')
        disciplina_id = request.POST.get('disciplina')
        sala_id = request.POST.get('sala')

        if not all([aula_id, professor_id, disciplina_id, sala_id]):
            return JsonResponse({'error': 'Todos os campos são obrigatórios.'}, status=400)

        aula = get_object_or_404(Aula, pk=aula_id)
        aula.professor_id = professor_id
        aula.disciplina_id = disciplina_id
        aula.sala_id = sala_id
        aula.save()
        
        return JsonResponse({
            'id': aula.id,
            'text': str(aula)
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# Helper to create views dynamically or just list them out. 
# Listing them out is explicit and better for maintenance.

# Professor
class ProfessorListView(ListView):
    model = Professor
    template_name = 'cadastro/professor_list.html'

class ProfessorCreateView(CreateView):
    model = Professor
    form_class = ProfessorForm
    template_name = 'cadastro/professor_form.html'
    success_url = reverse_lazy('professor_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dias = DiaSemana.objects.all().order_by('posicao')
        tempos = Tempo.objects.all().order_by('posicao')
        from .models import DiaTempoPermitido
        slots = DiaTempoPermitido.objects.all()
        slot_map = {(s.dia_id, s.tempo_id): s.id for s in slots}
        
        selected_ids = []
        if self.object:
            selected_ids = list(self.object.dias_proibidos.values_list('id', flat=True))
        
        grid_rows = []
        for tempo in tempos:
            row_slots = []
            for dia in dias:
                slot_id = slot_map.get((dia.id, tempo.id))
                is_checked = slot_id in selected_ids if slot_id else False
                row_slots.append({
                    'dia': dia,
                    'slot_id': slot_id,
                    'is_checked': is_checked
                })
            grid_rows.append({'tempo': tempo, 'slots': row_slots})
            
        context['dias_semana'] = dias
        context['grid_rows'] = grid_rows
        return context

class ProfessorUpdateView(UpdateView):
    model = Professor
    form_class = ProfessorForm
    template_name = 'cadastro/professor_form.html'
    success_url = reverse_lazy('professor_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dias = DiaSemana.objects.all().order_by('posicao')
        tempos = Tempo.objects.all().order_by('posicao')
        from .models import DiaTempoPermitido
        slots = DiaTempoPermitido.objects.all()
        slot_map = {(s.dia_id, s.tempo_id): s.id for s in slots}
        
        selected_ids = []
        if self.object:
            selected_ids = list(self.object.dias_proibidos.values_list('id', flat=True))
            
        grid_rows = []
        for tempo in tempos:
            row_slots = []
            for dia in dias:
                slot_id = slot_map.get((dia.id, tempo.id))
                is_checked = slot_id in selected_ids if slot_id else False
                row_slots.append({
                    'dia': dia,
                    'slot_id': slot_id,
                    'is_checked': is_checked
                })
            grid_rows.append({'tempo': tempo, 'slots': row_slots})
            
        context['dias_semana'] = dias
        context['grid_rows'] = grid_rows
        return context

class ProfessorDeleteView(DeleteView):
    model = Professor
    template_name = 'cadastro/professor_confirm_delete.html'
    success_url = reverse_lazy('professor_list')

# Disciplinas
class DisciplinasListView(ListView):
    model = Disciplinas
    template_name = 'cadastro/disciplinas_list.html'

class DisciplinasCreateView(CreateView):
    model = Disciplinas
    form_class = DisciplinasForm
    template_name = 'cadastro/disciplinas_form.html'
    success_url = reverse_lazy('disciplinas_list')

class DisciplinasUpdateView(UpdateView):
    model = Disciplinas
    form_class = DisciplinasForm
    template_name = 'cadastro/disciplinas_form.html'
    success_url = reverse_lazy('disciplinas_list')

class DisciplinasDeleteView(DeleteView):
    model = Disciplinas
    template_name = 'cadastro/disciplinas_confirm_delete.html'
    success_url = reverse_lazy('disciplinas_list')

# Tempo
class TempoListView(ListView):
    model = Tempo
    template_name = 'cadastro/tempo_list.html'

class TempoCreateView(CreateView):
    model = Tempo
    form_class = TempoForm
    template_name = 'cadastro/tempo_form.html'
    success_url = reverse_lazy('tempo_list')

class TempoUpdateView(UpdateView):
    model = Tempo
    form_class = TempoForm
    template_name = 'cadastro/tempo_form.html'
    success_url = reverse_lazy('tempo_list')

class TempoDeleteView(DeleteView):
    model = Tempo
    template_name = 'cadastro/tempo_confirm_delete.html'
    success_url = reverse_lazy('tempo_list')

# Aula
class AulaListView(ListView):
    model = Aula
    template_name = 'cadastro/aula_list.html'

class AulaCreateView(CreateView):
    model = Aula
    form_class = AulaForm
    template_name = 'cadastro/aula_form.html'
    success_url = reverse_lazy('aula_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dias = DiaSemana.objects.all().order_by('posicao')
        tempos = Tempo.objects.all().order_by('posicao')
        from .models import DiaTempoPermitido
        slots = DiaTempoPermitido.objects.all()
        slot_map = {(s.dia_id, s.tempo_id): s.id for s in slots}
        
        selected_ids = []
        if self.object:
            selected_ids = list(self.object.horarios.values_list('id', flat=True))
        
        grid_rows = []
        for tempo in tempos:
            row_slots = []
            for dia in dias:
                slot_id = slot_map.get((dia.id, tempo.id))
                is_checked = slot_id in selected_ids if slot_id else False
                row_slots.append({
                    'dia': dia,
                    'slot_id': slot_id,
                    'is_checked': is_checked
                })
            grid_rows.append({'tempo': tempo, 'slots': row_slots})
            
        context['dias_semana'] = dias
        context['grid_rows'] = grid_rows
        return context

class AulaUpdateView(UpdateView):
    model = Aula
    form_class = AulaForm
    template_name = 'cadastro/aula_form.html'
    success_url = reverse_lazy('aula_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dias = DiaSemana.objects.all().order_by('posicao')
        tempos = Tempo.objects.all().order_by('posicao')
        from .models import DiaTempoPermitido
        slots = DiaTempoPermitido.objects.all()
        slot_map = {(s.dia_id, s.tempo_id): s.id for s in slots}
        
        selected_ids = []
        if self.object:
            selected_ids = list(self.object.horarios.values_list('id', flat=True))
            
        grid_rows = []
        for tempo in tempos:
            row_slots = []
            for dia in dias:
                slot_id = slot_map.get((dia.id, tempo.id))
                is_checked = slot_id in selected_ids if slot_id else False
                row_slots.append({
                    'dia': dia,
                    'slot_id': slot_id,
                    'is_checked': is_checked
                })
            grid_rows.append({'tempo': tempo, 'slots': row_slots})
            
        context['dias_semana'] = dias
        context['grid_rows'] = grid_rows
        return context

class AulaDeleteView(DeleteView):
    model = Aula
    template_name = 'cadastro/aula_confirm_delete.html'
    success_url = reverse_lazy('aula_list')

# Turma
class TurmaListView(ListView):
    model = Turma
    template_name = 'cadastro/turma_list.html'

class TurmaCreateView(CreateView):
    model = Turma
    form_class = TurmaForm
    template_name = 'cadastro/turma_form.html'
    success_url = reverse_lazy('turma_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dias = DiaSemana.objects.all().order_by('posicao')
        tempos = Tempo.objects.all().order_by('posicao')
        from .models import DiaTempoPermitido
        slots = DiaTempoPermitido.objects.all()
        slot_map = {(s.dia_id, s.tempo_id): s.id for s in slots}
        
        # Determine selected slots
        selected_ids = []
        if self.object:
            selected_ids = list(self.object.dias.values_list('id', flat=True))
        
        grid_rows = []
        for tempo in tempos:
            row_slots = []
            for dia in dias:
                slot_id = slot_map.get((dia.id, tempo.id))
                is_checked = slot_id in selected_ids if slot_id else False
                row_slots.append({
                    'dia': dia,
                    'slot_id': slot_id,
                    'is_checked': is_checked
                })
            grid_rows.append({'tempo': tempo, 'slots': row_slots})
            
        context['dias_semana'] = dias
        context['grid_rows'] = grid_rows
        context['professores'] = Professor.objects.all()
        context['disciplinas'] = Disciplinas.objects.all()
        context['salas'] = Sala.objects.all()
        return context

class TurmaUpdateView(UpdateView):
    model = Turma
    form_class = TurmaForm
    template_name = 'cadastro/turma_form.html'
    success_url = reverse_lazy('turma_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dias = DiaSemana.objects.all().order_by('posicao')
        tempos = Tempo.objects.all().order_by('posicao')
        from .models import DiaTempoPermitido
        slots = DiaTempoPermitido.objects.all()
        slot_map = {(s.dia_id, s.tempo_id): s.id for s in slots}
        
        selected_ids = []
        if self.object:
            selected_ids = list(self.object.dias.values_list('id', flat=True))
            
        grid_rows = []
        for tempo in tempos:
            row_slots = []
            for dia in dias:
                slot_id = slot_map.get((dia.id, tempo.id))
                is_checked = slot_id in selected_ids if slot_id else False
                row_slots.append({
                    'dia': dia,
                    'slot_id': slot_id,
                    'is_checked': is_checked
                })
            grid_rows.append({'tempo': tempo, 'slots': row_slots})
            
        context['dias_semana'] = dias
        context['grid_rows'] = grid_rows
        context['professores'] = Professor.objects.all()
        context['disciplinas'] = Disciplinas.objects.all()
        context['salas'] = Sala.objects.all()
        return context

class TurmaDeleteView(DeleteView):
    model = Turma
    template_name = 'cadastro/turma_confirm_delete.html'
    success_url = reverse_lazy('turma_list')

# DiaSemana
class DiaSemanaListView(ListView):
    model = DiaSemana
    template_name = 'cadastro/diasemana_list.html'

class DiaSemanaCreateView(CreateView):
    model = DiaSemana
    form_class = DiaSemanaForm
    template_name = 'cadastro/diasemana_form.html'
    success_url = reverse_lazy('diasemana_list')

class DiaSemanaUpdateView(UpdateView):
    model = DiaSemana
    form_class = DiaSemanaForm
    template_name = 'cadastro/diasemana_form.html'
    success_url = reverse_lazy('diasemana_list')

class DiaSemanaDeleteView(DeleteView):
    model = DiaSemana
    template_name = 'cadastro/diasemana_confirm_delete.html'
    success_url = reverse_lazy('diasemana_list')

# Semestre
class SemestreListView(ListView):
    model = Semestre
    template_name = 'cadastro/semestre_list.html'

class SemestreCreateView(CreateView):
    model = Semestre
    form_class = SemestreForm
    template_name = 'cadastro/semestre_form.html'
    success_url = reverse_lazy('semestre_list')

class SemestreUpdateView(UpdateView):
    model = Semestre
    form_class = SemestreForm
    template_name = 'cadastro/semestre_form.html'
    success_url = reverse_lazy('semestre_list')

class SemestreDeleteView(DeleteView):
    model = Semestre
    template_name = 'cadastro/semestre_confirm_delete.html'
    success_url = reverse_lazy('semestre_list')

# Predio
class PredioListView(ListView):
    model = Predio
    template_name = 'cadastro/predio_list.html'

class PredioCreateView(CreateView):
    model = Predio
    form_class = PredioForm
    template_name = 'cadastro/predio_form.html'
    success_url = reverse_lazy('predio_list')

class PredioUpdateView(UpdateView):
    model = Predio
    form_class = PredioForm
    template_name = 'cadastro/predio_form.html'
    success_url = reverse_lazy('predio_list')

class PredioDeleteView(DeleteView):
    model = Predio
    template_name = 'cadastro/predio_confirm_delete.html'
    success_url = reverse_lazy('predio_list')

# Sala
class SalaListView(ListView):
    model = Sala
    template_name = 'cadastro/sala_list.html'

class SalaCreateView(CreateView):
    model = Sala
    form_class = SalaForm
    template_name = 'cadastro/sala_form.html'
    success_url = reverse_lazy('sala_list')

class SalaUpdateView(UpdateView):
    model = Sala
    form_class = SalaForm
    template_name = 'cadastro/sala_form.html'
    success_url = reverse_lazy('sala_list')

class SalaDeleteView(DeleteView):
    model = Sala
    template_name = 'cadastro/sala_confirm_delete.html'
    success_url = reverse_lazy('sala_list')
