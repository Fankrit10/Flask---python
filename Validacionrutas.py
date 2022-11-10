from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo, primer commit'

@app.route('/saluda')
def saluda():
    return 'Hola mundo, primer commit con saludo'

@app.route('/params/<int:name>/')
def params(name):
    return 'Hola mundo, primer commit con saludo {} '.format(name)

if __name__=='__main__':
    app.run(debug=True, port = 9000)
