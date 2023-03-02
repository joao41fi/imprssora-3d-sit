import os
import time

# Inicia o Pronsole
os.system("pronsole -n -p /dev/ttyACM0 -b 250000 &")

# Aguarda alguns segundos para o Pronsole iniciar
time.sleep(5)

# Envia um comando G-code para a impressora 3D
os.system("echo G28 > /tmp/pipe_pronsole")

# Aguarda a impressora 3D terminar de executar o comando
time.sleep(2)

# Envia outro comando G-code para a impressora 3D
os.system("echo G1 X10 Y10 Z0.3 F1000 > /tmp/pipe_pronsole")

# Aguarda a impressora 3D terminar de executar o comando
time.sleep(2)

# Fecha o Pronsole
os.system("echo quit > /tmp/pipe_pronsole")