from django.shortcuts import render
import calendar
from datetime import datetime
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Event, TipoEventos
from .forms import EventForm, TipoEventosForm

def index(request):
    # Get year and month from request, default to current
    today = datetime.today()
    try:
        year = int(request.GET.get('year', today.year))
        month = int(request.GET.get('month', today.month))
    except ValueError:
        year = today.year
        month = today.month

    # Adjust month if out of bounds (handle navigation)
    if month > 12:
        month = 1
        year += 1
    elif month < 1:
        month = 12
        year -= 1

    # Create calendar object
    cal = calendar.Calendar(firstweekday=6) # 6 = Sunday
    month_days = cal.monthdayscalendar(year, month)

    # Portuguese month names
    MONTH_NAMES = {
        1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
        5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
        9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
    }
    month_name = MONTH_NAMES.get(month, '')
    
    # Calculate previous and next month for navigation
    prev_month = month - 1
    prev_year = year
    if prev_month < 1:
        prev_month = 12
        prev_year -= 1
        
    next_month = month + 1
    next_year = year
    if next_month > 12:
        next_month = 1
        next_year += 1

    context = {
        'year': year,
        'month': month,
        'month_name': month_name,
        'calendar_weeks': month_days,
        'prev_year': prev_year,
        'prev_month': prev_month,
        'next_year': next_year,
        'next_month': next_month,
    }

    return render(request, 'calendario/index.html', context)

# Event
class EventListView(ListView):
    model = Event
    template_name = 'calendario/event_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(title__icontains=q)
        return queryset

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'calendario/event_form.html'
    success_url = reverse_lazy('event_list')

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'calendario/event_form.html'
    success_url = reverse_lazy('event_list')

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'calendario/event_confirm_delete.html'
    success_url = reverse_lazy('event_list')

# TipoEventos
class TipoEventosListView(ListView):
    model = TipoEventos
    template_name = 'calendario/tipoeventos_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(nome__icontains=q)
        return queryset

class TipoEventosCreateView(CreateView):
    model = TipoEventos
    form_class = TipoEventosForm
    template_name = 'calendario/tipoeventos_form.html'
    success_url = reverse_lazy('tipoeventos_list')

class TipoEventosUpdateView(UpdateView):
    model = TipoEventos
    form_class = TipoEventosForm
    template_name = 'calendario/tipoeventos_form.html'
    success_url = reverse_lazy('tipoeventos_list')

class TipoEventosDeleteView(DeleteView):
    model = TipoEventos
    template_name = 'calendario/tipoeventos_confirm_delete.html'
    success_url = reverse_lazy('tipoeventos_list')