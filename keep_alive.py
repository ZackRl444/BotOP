from flask import Flask
from threading import Thread
from flask import send_file

app = Flask('')

@app.route('/download')
def download_file():
    return send_file('/workspace/inventory.db', as_attachment=True)

@app.route('/')
def home():
    return "Le bot est en ligne !"

def run():
    app.run(host='0.0.0.0', port=5000)

def keep_alive():
    t = Thread(target=run)
    t.start()
