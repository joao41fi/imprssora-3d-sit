#!/usr/bin/env python


from flask import *
from scrpt import *
import os
import time
import os
import sys

meus_modulos_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'db'))
sys.path.insert(0, meus_modulos_dir)

from  ler_tabela import *
from atualizar import *

meus_modulos_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'script'))
sys.path.insert(0, meus_modulos_dir)
from defes import *

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
			ficheiro =abrir('main/ficheiro.db','fichieros')
			
			imprimir(ficheiro[0][0])
			
            
			#result = subprocess.run(["G28"], capture_output=True)
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
    caminho = 'uploads/' + file.filename
    atualizar_tabela("main/ficheiro.db", "fichieros", "FICH ",caminho)
    file.save('uploads/' + file.filename)
    return render_template('index.html')

app.run(debug=True,host='0.0.0.0')