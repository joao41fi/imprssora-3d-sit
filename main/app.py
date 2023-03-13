#!/usr/bin/env python

from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google
import logging
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

load_dotenv()
app = Flask(__name__)


client_id = '652183645625-uk4cvnoqmhqa6lao9oki2g5j49gcc2e6.apps.googleusercontent.com'
client_secret = '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'
app.secret_key = "\\\x8eY\xf5\xab=\r.-\xbe\xe3}~\xc7\x19\x05z\xf4\xb5=\xfa\xf4"

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

blueprint = make_google_blueprint(
    client_id=client_id,
    client_secret=client_secret,
    reprompt_consent=True,
    scope=["profile", "email"]
)
app.register_blueprint(blueprint, url_prefix="/login")

@app.route("/")
def index():
    google_data = None
    user_info_endpoint = '/oauth2/v2/userinfo'
    if google.authorized:
        google_data = google.get(user_info_endpoint).json()
    print(google_data)
    return render_template('index.j2',
                           google_data=google_data,
                           fetch_url=google.base_url + user_info_endpoint)
    #return render_template(index.html)

@app.route('/login')
def login():
    return redirect(url_for('google.login'))

@app.route('/other')
def other():
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
    caminho(6,nova)  
    file.save('/home/joao41/Desktop/imprssora-3d-sit/main/uploads/' + file.filename)
   
    return render_template('index.html')

@app.route('/temp', methods=['POST'])
def update_number():
    # Obter o número a partir do formulário
    number = int(request.form['number'])
    # Executar a função para atualizar o número
    comandos('M109 S200')
    # Renderizar a página com o novo número
    return render_template('index.html', number=number)

@app.route('/button', methods=['POST'])
def button():
    button_id = request.form['button_id']
    print(button_id)
    comandos('G1 X10')
    return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')
