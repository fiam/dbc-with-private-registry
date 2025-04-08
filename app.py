from flask import Flask
from datetime import datetime
import signal
import sys
import os

app = Flask(__name__)

@app.route('/')
def hello():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    version = os.getenv('VERSION')
    if not version:
        version = 'unknown'
    return f'Hello! Version {version}, current server time is {now}'

@app.route('/healthz')
def healthz():
    return 'OK', 200

def handle_shutdown(signum, frame):
    print(f"Received signal {signum}, shutting down.")
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, handle_shutdown)
    signal.signal(signal.SIGTERM, handle_shutdown)
    app.run(host='0.0.0.0', port=5001)
