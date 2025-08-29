from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"  # Sadece basit bir metin döndür

def keep_alive():
    import threading
    thread = threading.Thread(target=lambda: app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False))
    thread.daemon = True
    thread.start()
