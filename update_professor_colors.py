import os
import django
import random
import sys

# Add the project directory to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'GestorDoTempo'))

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GestorDoTempo.settings')
django.setup()

from cadastro.models import Professor

def generate_unique_color(used_colors):
    """Generates a random hex color that hasn't been used yet."""
    while True:
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        if color not in used_colors:
            return color

def update_colors():
    professors = Professor.objects.all()
    used_colors = set()
    
    # Pre-fill used_colors with existing colors if we wanted to keep some, 
    # but here we will just overwrite all to ensure uniqueness among the set.
    # Or better, let's just re-assign all of them.
    
    count = 0
    for professor in professors:
        new_color = generate_unique_color(used_colors)
        professor.cor = new_color
        professor.save()
        used_colors.add(new_color)
        count += 1
        
    print(f"Updated colors for {count} professors.")

if __name__ == '__main__':
    update_colors()
