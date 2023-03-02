from flask import *
import subprocess
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/Ligar_Impresora', methods=['POST'])

def Ligar_Impresora():
	if 'checkbox_funcao' in request.form:
		if request.form['checkbox_funcao'] == 'true':
			print('primeira')
			# Execute sua função aqui
			result = subprocess.run(["pronsole"], capture_output=True)
			output = result.stdout.decode()
			print(output)
			result = subprocess.run(["connect/dev/ttyACM0 250000"], capture_output=True)
			output = result.stdout.decode()
			print(output)
			result = subprocess.run(["G28"], capture_output=True)
			return jsonify({'mensagem': 'Função executada com sucesso!'})
		else:
			return jsonify({'mensagem': 'A caixa de seleção não foi marcada.'})
	else:
		return jsonify({'mensagem': 'Erro ao executar a função.'})


@app.route('/Ligar_Camara', methods=['POST'])
def Ligar_Camara():
	if 'checkbox_funcao' in request.form:
		if request.form['checkbox_funcao'] == 'true':
			print('camara on ')
			# Execute sua função aqui
			return jsonify({'mensagem': 'Função executada com sucesso!'})
		else:
			print('camara off ')
			return jsonify({'mensagem': 'A caixa de seleção não foi marcada.'})
	else:
		return jsonify({'mensagem': 'Erro ao executar a função.'})
	

@app.route('/executar-funcao-3', methods=['POST'])
def executar_funcao_3():
	if 'checkbox_funcao' in request.form:
		if request.form['checkbox_funcao'] == 'true':
			# Execute sua função aqui
			return jsonify({'mensagem': 'Função executada com sucesso!'})
		else:
			return jsonify({'mensagem': 'A caixa de seleção não foi marcada.'})
	else:
		return jsonify({'mensagem': 'Erro ao executar a função.'})
	
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save('uploads/' + file.filename)
    return render_template('index.html')

app.run(debug=True,host='0.0.0.0')