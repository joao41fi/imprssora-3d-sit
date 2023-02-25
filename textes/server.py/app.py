from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Processa solicitação GET
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_form():
    # Processa solicitação POST
    nome = request.form['nome']
    return render_template('index.html', nome=nome)

if __name__ == '__main__':
    app.run(debug=True)