import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/docker')
def docker():
    return 'Hello Docker'

@app.route('/kubernetes')
def kubernetes():
    return 'Hello Kubernetes'

@app.route('/healthz')
def healthz():
    return 'I am healthy'

@app.route('/readiness')
def readiness():
    return 'I am ready'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
