import os
import django
import csv
import random

import sys
# Add the project directory to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'GestorDoTempo'))

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GestorDoTempo.settings')
django.setup()

from cadastro.models import Professor

def generate_color():
    """Generates a random hex color."""
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def import_professores(csv_path):
    if not os.path.exists(csv_path):
        print(f"File not found: {csv_path}")
        return

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        
        # Clean up field names (strip whitespace)
        reader.fieldnames = [name.strip() for name in reader.fieldnames if name]
        
        count = 0
        for row in reader:
            # Map CSV columns to Model fields
            # CSV: #;Nome;Abreviacao;Telefone;E-mail;
            nome = row.get('Nome', '').strip()
            abreviatura = row.get('Abreviacao', '').strip()[:20] # Truncate to 20 chars
            telefone = row.get('Telefone', '').strip()[:20] # Truncate to 20 chars
            email = row.get('E-mail', '').strip()
            
            if not email:
                print(f"Skipping row without email: {row}")
                continue

            # Check if professor already exists
            if Professor.objects.filter(email=email).exists():
                print(f"Professor already exists: {nome} ({email})")
                continue

            # Create new professor
            professor = Professor(
                nome=nome,
                abreviatura=abreviatura,
                telefone=telefone,
                email=email,
                senha='123', # Default password
                cor=generate_color()
            )
            professor.save()
            print(f"Created: {nome}")
            count += 1

    print(f"Import completed. {count} professors added.")

if __name__ == '__main__':
    csv_file = 'Relatorio.csv'
    import_professores(csv_file)
