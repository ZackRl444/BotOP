import sqlite3

BACKUP_FILE = "inventory_backup.sql"
DB_FILE = "inventory.db"

def restore_database():
    try:
        with open(BACKUP_FILE, 'r') as f:
            sql_script = f.read()

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.executescript(sql_script)
        conn.commit()
        conn.close()

        print(f"Base de données restaurée depuis : {BACKUP_FILE}")
    except FileNotFoundError:
        print(f"Aucune sauvegarde trouvée ({BACKUP_FILE}), démarrage avec une base vide.")
    except Exception as e:
        print(f"Erreur lors de la restauration : {e}")

if __name__ == "__main__":
    restore_database()
