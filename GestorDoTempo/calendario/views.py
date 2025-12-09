from django.contrib.auth.mixins import LoginRequiredMixin
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

    # Get events for this month
    from .models import EventDate
    
    events_in_month = EventDate.objects.filter(
        date__year=year, 
        date__month=month
    ).select_related('event', 'event__tipo')
    
    events_map = {}
    for event_date in events_in_month:
        day = event_date.date.day
        if day not in events_map:
            # Store event details
            events_map[day] = {
                'color': event_date.event.tipo.cor,
                'title': event_date.event.title,
                'description': event_date.event.description or 'Sem descrição',
                'type': event_date.event.tipo.nome
            }

    context = {
        'year': year,
        'month': month,
        'month_name': month_name,
        'calendar_weeks': month_days,
        'prev_year': prev_year,
        'prev_month': prev_month,
        'next_year': next_year,
        'next_month': next_month,
        'events_map': events_map,
    }

    return render(request, 'calendario/index.html', context)

# Event
class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'calendario/event_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(title__icontains=q)
        return queryset

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'calendario/event_form.html'
    success_url = reverse_lazy('event_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        selected_dates = self.request.POST.get('selected_dates', '')
        if selected_dates:
            from .models import EventDate
            dates = selected_dates.split(',')
            for date_str in dates:
                if date_str:
                    EventDate.objects.create(event=self.object, date=date_str)
        return response

class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'calendario/event_form.html'
    success_url = reverse_lazy('event_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['existing_dates'] = list(self.object.dates.values_list('date', flat=True))
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        selected_dates = self.request.POST.get('selected_dates', '')
        if selected_dates:
            from .models import EventDate
            # Clear existing dates and add new ones
            self.object.dates.all().delete()
            dates = selected_dates.split(',')
            for date_str in dates:
                if date_str:
                    EventDate.objects.create(event=self.object, date=date_str)
        else:
            # If empty, it might mean all dates were removed
            self.object.dates.all().delete()
        return response

class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = 'calendario/event_confirm_delete.html'
    success_url = reverse_lazy('event_list')

# TipoEventos
class TipoEventosListView(LoginRequiredMixin, ListView):
    model = TipoEventos
    template_name = 'calendario/tipoeventos_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(nome__icontains=q)
        return queryset

class TipoEventosCreateView(LoginRequiredMixin, CreateView):
    model = TipoEventos
    form_class = TipoEventosForm
    template_name = 'calendario/tipoeventos_form.html'
    success_url = reverse_lazy('tipoeventos_list')

class TipoEventosUpdateView(LoginRequiredMixin, UpdateView):
    model = TipoEventos
    form_class = TipoEventosForm
    template_name = 'calendario/tipoeventos_form.html'
    success_url = reverse_lazy('tipoeventos_list')

class TipoEventosDeleteView(LoginRequiredMixin, DeleteView):
    model = TipoEventos
    template_name = 'calendario/tipoeventos_confirm_delete.html'
    success_url = reverse_lazy('tipoeventos_list')