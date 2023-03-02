import os
import time

# Inicia o Pronsole
os.system("cd /")
os.system("pronsole")

# Aguarda alguns segundos para o Pronsole iniciar
time.sleep(5)

# Estabelece uma conexão com a impressora 3D
os.system("echo connect ")

# Aguarda a conexão ser estabelecida
time.sleep(2)

# Envia um comando G-code para a impressora 3D
os.system("echo G28")

# Aguarda a impressora 3D terminar de executar o comando
time.sleep(2)

# Envia outro comando G-code para a impressora 3D
os.system("echo G1 X10 Y10 Z0.3 F1000 «")

# Aguarda a impressora 3D terminar de executar o comando
time.sleep(2)

# Fecha o Pronsole
os.system("echo quit")