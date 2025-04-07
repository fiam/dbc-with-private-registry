from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f'Hello! Current server time is {now}'

@app.route('/healthz')
def healthz():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

