from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola, mundo!'

@app.route('/adios')
def bye():
    return 'Hasta luego!'

@app.route ('/bebi')
def bebi():
    return 'Hola bebieta tan boñeta, te amo muuuuuuuusho'