from django.urls import path
from . import views
from .views import (
    EventListView, EventCreateView, EventUpdateView, EventDeleteView,
    TipoEventosListView, TipoEventosCreateView, TipoEventosUpdateView, TipoEventosDeleteView
)

urlpatterns = [
    path('', views.index, name='index'),
    
    # Event
    path('event/', EventListView.as_view(), name='event_list'),
    path('event/novo/', EventCreateView.as_view(), name='event_create'),
    path('event/<int:pk>/editar/', EventUpdateView.as_view(), name='event_update'),
    path('event/<int:pk>/excluir/', EventDeleteView.as_view(), name='event_delete'),

    # TipoEventos
    path('tipoeventos/', TipoEventosListView.as_view(), name='tipoeventos_list'),
    path('tipoeventos/novo/', TipoEventosCreateView.as_view(), name='tipoeventos_create'),
    path('tipoeventos/<int:pk>/editar/', TipoEventosUpdateView.as_view(), name='tipoeventos_update'),
    path('tipoeventos/<int:pk>/excluir/', TipoEventosDeleteView.as_view(), name='tipoeventos_delete'),
]
