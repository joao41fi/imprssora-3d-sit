import serial
import time

# Configure a porta serial com as configurações adequadas para a impressora 3D
ser = serial.Serial('/dev/ttyACM0', 250000, timeout=1)

# Abre o arquivo G-code para leitura
with open('/home/joao41/Desktop/imprssora-3d-sit/arquivo.gcode', 'r') as f:
    # Loop através de cada linha do arquivo G-code
    for line in f:
        # Remove espaços em branco e quebras de linha
        line = line.strip()
        
        # Envia a linha para a impressora 3D
        ser.write(line.encode('utf-8') + b'\n')
        
        # Espera um breve momento para a impressora processar o comando
        time.sleep(0.1)

# Fechar a porta serial
ser.close()


