from django.core.management.base import BaseCommand
from backup_app.models import Data

class Command(BaseCommand):
    help = 'Vytvoří testovací data'

    def handle(self, *args, **kwargs):
        test_data = [
            "Test data 1 - dokument",
            "Test data 2 - faktura",
            "Test data 3 - zpráva",
        ]
        
        for text in test_data:
            Data.objects.create(text=text)
        
        self.stdout.write('Testovací data byla vytvořena!')