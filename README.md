# Backup Project

Jednoduchá Django aplikace pro vytváření záloh dat s podporou Dockeru.

## Spuštění lokálně

1. Vytvořte a aktivujte virtuální prostředí:
python -m venv venv
venv\Scripts\activate  # Windows
# nebo source venv/bin/activate  # Linux/Mac

2. Nainstalujte závislosti:
pip install django

3. Spusťte migrace:
python manage.py migrate

4. Spusťte server:
python manage.py runserver

## Spuštění v Dockeru

1. Sestavte Docker image:
docker build -t backup-project .

2. Spusťte kontejner:
docker run -p 8000:8000 backup-project

## Použití aplikace

1. Přidání testovacích dat:
- Navštivte http://localhost:8000/add-data/

2. Vytvoření zálohy:
- Navštivte http://localhost:8000/create/

3. Extrakce zálohy z Dockeru:
# Zjistěte ID kontejneru
docker ps

# Zkopírujte zálohu (nahraďte [ID_KONTEJNERU] skutečným ID)
docker cp [ID_KONTEJNERU]:/app/backups/backup.json ./docker_backup.json

## Struktura projektu
- backup_app/ - hlavní aplikace
- backup_project/ - nastavení projektu
- backups/ - složka pro zálohy
- Dockerfile - konfigurace pro Docker

## Požadavky
- Python 3.9 nebo vyšší
- Django 5.1.5
- Docker (pro spuštění v kontejneru)
