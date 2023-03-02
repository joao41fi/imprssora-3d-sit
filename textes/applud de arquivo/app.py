from flask import *

app = Flask(__name__)

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save('uploads/' + file.filename)
    return 'Arquivo enviado com sucesso!'
	
app.run(debug=True)