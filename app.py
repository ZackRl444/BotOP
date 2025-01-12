from flask import Flask, send_file

app = Flask(__name__)

# Route pour télécharger le fichier
@app.route('/download')
def download_file():
    # Remplace le chemin par le chemin correct vers ton fichier
    file_path = '/workspace/inventory_backup.zip'
    return send_file(file_path, as_attachment=True)

# Lancer le serveur Flask sur l'adresse 0.0.0.0 et le port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
