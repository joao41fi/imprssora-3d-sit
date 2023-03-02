import os
import time

# Abre o Pronsole em um terminal separado
os.system("lxterminal -e pronsole &")

# Aguarda alguns segundos para o Pronsole inicializar
time.sleep(20)

# Envia um comando para o Pronsole
os.system("echo connect/dev/ttyACM0 250000 > /tmp/pipe_pronsole")
os.system("echo G28 > /tmp/pipe_pronsole")

# Lê a resposta do Pronsole
with open('/tmp/pipe_pronsole', 'r') as f:
    output = f.readline()
print(output)

# Fecha o terminal do Pronsole
os.system("pkill -f gnome-terminal")
