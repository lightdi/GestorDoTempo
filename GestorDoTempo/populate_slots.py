import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GestorDoTempo.settings')
django.setup()

from cadastro.models import DiaSemana, Tempo, DiaTempoPermitido

def populate():
    dias = DiaSemana.objects.all()
    tempos = Tempo.objects.all()
    
    count = 0
    for dia in dias:
        for tempo in tempos:
            obj, created = DiaTempoPermitido.objects.get_or_create(dia=dia, tempo=tempo)
            if created:
                count += 1
    
    print(f"Created {count} new DiaTempoPermitido slots.")

if __name__ == '__main__':
    populate()
