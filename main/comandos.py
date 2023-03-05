import subprocess
import time
import serial
# Executar um comando simples na console
#subprocess.run(["pronsole","-c","Desktop/imprssora-3d-sit/texte.cfg"])
import os

# Ejecutar un comando en CMD
os.system('pronsole -c Desktop/imprssora-3d-sit/texte.cfg')


resultado = os.popen('pronsole -c Desktop/imprssora-3d-sit/texte.cfg').read()
print(resultado)