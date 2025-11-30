from django.urls import path
from .views import (
    ProfessorListView, ProfessorCreateView, ProfessorUpdateView, ProfessorDeleteView,
    DisciplinasListView, DisciplinasCreateView, DisciplinasUpdateView, DisciplinasDeleteView,
    TempoListView, TempoCreateView, TempoUpdateView, TempoDeleteView,
    AulaListView, AulaCreateView, AulaUpdateView, AulaDeleteView,
    TurmaListView, TurmaCreateView, TurmaUpdateView, TurmaDeleteView,
    DiaSemanaListView, DiaSemanaCreateView, DiaSemanaUpdateView, DiaSemanaDeleteView,
    SemestreListView, SemestreCreateView, SemestreUpdateView, SemestreDeleteView,
    PredioListView, PredioCreateView, PredioUpdateView, PredioDeleteView,
    SalaListView, SalaCreateView, SalaUpdateView, SalaDeleteView,
    create_aula_ajax, get_aula_details_ajax, update_aula_ajax
)

urlpatterns = [
    # AJAX
    path('ajax/create-aula/', create_aula_ajax, name='create_aula_ajax'),
    path('ajax/get-aula-details/<int:pk>/', get_aula_details_ajax, name='get_aula_details_ajax'),
    path('ajax/update-aula/', update_aula_ajax, name='update_aula_ajax'),

    # Professor
    path('professor/', ProfessorListView.as_view(), name='professor_list'),
    path('professor/novo/', ProfessorCreateView.as_view(), name='professor_create'),
    path('professor/<int:pk>/editar/', ProfessorUpdateView.as_view(), name='professor_update'),
    path('professor/<int:pk>/excluir/', ProfessorDeleteView.as_view(), name='professor_delete'),

    # Disciplinas
    path('disciplinas/', DisciplinasListView.as_view(), name='disciplinas_list'),
    path('disciplinas/novo/', DisciplinasCreateView.as_view(), name='disciplinas_create'),
    path('disciplinas/<int:pk>/editar/', DisciplinasUpdateView.as_view(), name='disciplinas_update'),
    path('disciplinas/<int:pk>/excluir/', DisciplinasDeleteView.as_view(), name='disciplinas_delete'),

    # Tempo
    path('tempo/', TempoListView.as_view(), name='tempo_list'),
    path('tempo/novo/', TempoCreateView.as_view(), name='tempo_create'),
    path('tempo/<int:pk>/editar/', TempoUpdateView.as_view(), name='tempo_update'),
    path('tempo/<int:pk>/excluir/', TempoDeleteView.as_view(), name='tempo_delete'),

    # Aula
    path('aula/', AulaListView.as_view(), name='aula_list'),
    path('aula/novo/', AulaCreateView.as_view(), name='aula_create'),
    path('aula/<int:pk>/editar/', AulaUpdateView.as_view(), name='aula_update'),
    path('aula/<int:pk>/excluir/', AulaDeleteView.as_view(), name='aula_delete'),

    # Turma
    path('turma/', TurmaListView.as_view(), name='turma_list'),
    path('turma/novo/', TurmaCreateView.as_view(), name='turma_create'),
    path('turma/<int:pk>/editar/', TurmaUpdateView.as_view(), name='turma_update'),
    path('turma/<int:pk>/excluir/', TurmaDeleteView.as_view(), name='turma_delete'),

    # DiaSemana
    path('diasemana/', DiaSemanaListView.as_view(), name='diasemana_list'),
    path('diasemana/novo/', DiaSemanaCreateView.as_view(), name='diasemana_create'),
    path('diasemana/<int:pk>/editar/', DiaSemanaUpdateView.as_view(), name='diasemana_update'),
    path('diasemana/<int:pk>/excluir/', DiaSemanaDeleteView.as_view(), name='diasemana_delete'),

    # Semestre
    path('semestre/', SemestreListView.as_view(), name='semestre_list'),
    path('semestre/novo/', SemestreCreateView.as_view(), name='semestre_create'),
    path('semestre/<int:pk>/editar/', SemestreUpdateView.as_view(), name='semestre_update'),
    path('semestre/<int:pk>/excluir/', SemestreDeleteView.as_view(), name='semestre_delete'),

    # Predio
    path('predio/', PredioListView.as_view(), name='predio_list'),
    path('predio/novo/', PredioCreateView.as_view(), name='predio_create'),
    path('predio/<int:pk>/editar/', PredioUpdateView.as_view(), name='predio_update'),
    path('predio/<int:pk>/excluir/', PredioDeleteView.as_view(), name='predio_delete'),

    # Sala
    path('sala/', SalaListView.as_view(), name='sala_list'),
    path('sala/novo/', SalaCreateView.as_view(), name='sala_create'),
    path('sala/<int:pk>/editar/', SalaUpdateView.as_view(), name='sala_update'),
    path('sala/<int:pk>/excluir/', SalaDeleteView.as_view(), name='sala_delete'),
]
