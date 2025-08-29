from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Render otomatik olarak environment variable'dan alır
    return f"✅ Bot aktif! Render URL: {os.environ.get('RENDER_EXTERNAL_URL', 'Bilinmiyor')}"

def keep_alive():
    # Port'u Render'ın istediği şekilde ayarla
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
