from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo, primer commit'

@app.route('/saluda')
def saluda():
    return 'Hola mundo, primer commit con saludo'

@app.route('/params')
def params():
    parametro1=request.args.get('params1','no hay')
    return 'Hola mundo, primer commit con saludo {} '.format(parametro1)

if __name__=='__main__':
    app.run(debug=True, port = 8000)
