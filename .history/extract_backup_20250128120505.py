import subprocess
import os

def extract_backup():
    try:
        # Získat ID kontejneru
        container_id = subprocess.check_output(
            ["docker", "ps", "-q", "-f", "ancestor=backup-project"]
        ).decode().strip()
        
        # Vytvořit složku pro extrahované zálohy
        os.makedirs('extracted_backups', exist_ok=True)
        
        # Kopírovat zálohy z Dockeru
        subprocess.run([
            "docker", "cp",
            f"{container_id}:/app/backups/.",
            "./extracted_backups/"
        ])
        
        print('Zálohy byly úspěšně extrahovány do složky extracted_backups/')
        
    except Exception as e:
        print(f'Chyba při extrakci zálohy: {e}')

if __name__ == "__main__":
    extract_backup()