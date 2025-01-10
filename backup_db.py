import os
import sqlite3
import subprocess

# Configurations
DB_PATH = 'inventory.db'  # Chemin de la base SQLite (modifie si nécessaire)
BACKUP_FILE = 'inventory_backup.sql'   # Nom du fichier de sauvegarde
COMMIT_MESSAGE = 'Sauvegarde automatique de la base de données'  # Message de commit

def backup_database():
    """Exporte la base SQLite vers un fichier SQL."""
    if os.path.exists(DB_PATH):
        try:
            conn = sqlite3.connect(DB_PATH)
            with open(BACKUP_FILE, 'w') as f:
                for line in conn.iterdump():
                    f.write(f'{line}\n')
            print(f"Sauvegarde réussie dans le fichier : {BACKUP_FILE}")
        except Exception as e:
            print(f"Erreur lors de l'exportation : {e}")
        finally:
            conn.close()
    else:
        print(f"Base de données introuvable à l'emplacement : {DB_PATH}")

def push_to_github():
    """Ajoute le fichier de sauvegarde au dépôt GitHub et le push."""
    try:
        # Étape 1 : Ajouter le fichier au suivi Git
        subprocess.run(['git', 'add', BACKUP_FILE], check=True)

        # Étape 2 : Créer un commit
        subprocess.run(['git', 'commit', '-m', COMMIT_MESSAGE], check=True)

        # Étape 3 : Envoyer les changements sur le dépôt distant
        subprocess.run(['git', 'push', 'origin', 'main'], check=True)
        print("Fichier de sauvegarde envoyé sur GitHub avec succès.")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'envoi sur GitHub : {e}")

if __name__ == "__main__":
    backup_database()
    push_to_github()