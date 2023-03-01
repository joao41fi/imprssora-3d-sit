from flask import *

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/executar-funcao-1', methods=['POST'])
def executar_funcao_1():
	if 'checkbox_funcao' in request.form:
		if request.form['checkbox_funcao'] == 'true':
			print('primeira')
			# Execute sua função aqui
			return jsonify({'mensagem': 'Função executada com sucesso!'})
		else:
			return jsonify({'mensagem': 'A caixa de seleção não foi marcada.'})
	else:
		return jsonify({'mensagem': 'Erro ao executar a função.'})


@app.route('/executar-funcao-2', methods=['POST'])
def executar_funcao_2():
	if 'checkbox_funcao' in request.form:
		if request.form['checkbox_funcao'] == 'true':
			# Execute sua função aqui
			return jsonify({'mensagem': 'Função executada com sucesso!'})
		else:
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
	
app.run(debug=True)