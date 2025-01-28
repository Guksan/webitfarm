from django.http import HttpResponse
from .models import Data
import json
import os

def create_backup(request):
    # Vezme data z databáze
    data = list(Data.objects.all().values())
    
    # Vytvoří složku pro zálohy pokud neexistuje
    if not os.path.exists('backups'):
        os.makedirs('backups')
    
    # Uloží data do souboru
    with open('backups/backup.json', 'w') as f:
        json.dump(data, f)
    
    return HttpResponse('Záloha vytvořena!')

def add_test_data(request):
    Data.objects.create(text="Test data 1")
    Data.objects.create(text="Test data 2")
    return HttpResponse('Testovací data přidána')