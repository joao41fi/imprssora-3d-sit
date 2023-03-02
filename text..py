import os
import time

# Abre o Pronsole em um terminal separado
os.system("x-terminal-emulator -e pronsole")

# Aguarda alguns segundos para o Pronsole inicializar
time.sleep(2)

# Envia um comando para o Pronsole
os.system("echo G28 > /tmp/pipe_pronsole")

# Lê a resposta do Pronsole
with open('/tmp/pipe_pronsole', 'r') as f:
    output = f.readline()
print(output)

# Fecha o terminal do Pronsole
os.system("killall x-terminal-emulator")
