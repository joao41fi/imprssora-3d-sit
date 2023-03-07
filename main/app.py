#!/usr/bin/env python


from flask import *
import cv2
import os
import time
import sys
import threading
import subprocess

meus_modulos_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'db'))
sys.path.insert(0, meus_modulos_dir)

from  ler_tabela import *
from atualizar import *

meus_modulos_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'scrpts.py'))
sys.path.insert(0, meus_modulos_dir)
from defes import *
meus_modulos_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'main'))
sys.path.insert(0, meus_modulos_dir)

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
			ficheiro =abrir('/home/joao41/Desktop/imprssora-3d-sit/main/ficheiro.db','fichieros')
			print(ficheiro)
			#por os ficheiros a alterar 
			subprocess.run(["pronsole","-c","Desktop/imprssora-3d-sit/main/scrpts.py/texte.cfg"])

			
			
             
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
			home()
			return jsonify({'mensagem': 'Função executada com sucesso!'})
		else:
			return jsonify({'mensagem': 'A caixa de seleção não foi marcada.'})
	else:
		return jsonify({'mensagem': 'Erro ao executar a função.'})
	
@app.route('/upload', methods=['POST'])
def upload():
    
    file = request.files['file']
    ficheiro =abrir('/home/joao41/Desktop/imprssora-3d-sit/main/ficheiro.db','fichieros')
    caminhos = '/home/joao41/Desktop/imprssora-3d-sit/main/uploads/' + file.filename
    caminhos2 = 'Desktop/imprssora-3d-sit/main/uploads/' + file.filename
    atualizar_tabela("/home/joao41/Desktop/imprssora-3d-sit/main/ficheiro.db", "fichieros", "FICH ",caminhos)
    nova = 'load '+caminhos2
    velha = 'load Desktop/imprssora-3d-sit/main/'+ficheiro[0][0]
    print('velha-'+velha)
     # textar 
    caminho(nova,velha)  
    file.save('/home/joao41/Desktop/imprssora-3d-sit/main/uploads/' + file.filename)
   
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(get_frame(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')
