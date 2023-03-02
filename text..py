import os
import time

# Abre o Pronsole em um terminal separado
os.system("pronsole")

# Aguarda alguns segundos para o Pronsole inicializar
time.sleep(10)

# Envia um comando para o Pronsole
os.system("echo connect /dev/ttyACM0 250000")
os.system("echo G28")

# Lê a resposta do Pronsole
