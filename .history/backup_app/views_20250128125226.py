from django.http import HttpResponse
from .models import Data
import json
import os
from datetime import datetime

def create_backup(request):
    # Vezme data z databáze a převede datetime na string
    data = []
    for item in Data.objects.all():
        data.append({
            'id': item.id,
            'text': item.text,
            'created_at': item.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })
    
    # Vytvoří složku pro zálohy pokud neexistuje
    if not os.path.exists('backups'):
        os.makedirs('backups')
    
    # Uloží data do souboru
    with open('backups/backup.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    return HttpResponse('Záloha vytvořena!')