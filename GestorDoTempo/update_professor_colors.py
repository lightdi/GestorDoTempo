import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GestorDoTempo.settings')
django.setup()

from cadastro.models import Professor

def generate_random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def update_colors():
    professors = Professor.objects.all()
    count = 0
    for professor in professors:
        if not professor.cor or professor.cor == '#FFFFFF': # Update if empty or default white
            professor.cor = generate_random_color()
            professor.save()
            count += 1
            print(f"Updated {professor.nome} with color {professor.cor}")
    
    print(f"Successfully updated {count} professors.")

if __name__ == '__main__':
    update_colors()
