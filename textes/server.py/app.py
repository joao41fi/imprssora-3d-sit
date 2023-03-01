from flask import Flask, request, render_template
from scripts.info import *

app = Flask(__name__)
global nome

@app.route('/', methods=['GET'])
def index():
    # Processa solicitação GET
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_form():
    # Processa solicitação POST

    
    nome = request.form['nome']
    save('texte.pickle',nome)


    return render_template('index.html', nome=nome)

@app.route('/but2', methods=['POST'])
def but2():
    # Processa solicitação POST
    
    nome = tras('texte.pickle')
    return render_template('index.html',nome=nome)

@app.route('/on',  methods=['POST'])
def on():
    if request.form.getlist('match')[0] == 'world':
      print('marcado')
    return render_template('index.html')
    


if __name__ == '__main__':
    app.run(debug=True)

