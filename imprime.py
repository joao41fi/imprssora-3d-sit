import serial
import time

# Configure a porta serial com as configurações adequadas para a impressora 3D
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

# Abra o arquivo G-code e leia seu conteúdo
with open('arquivo.gcode', 'r') as f:
    gcode = f.readlines()

# Envie cada linha do arquivo G-code para a impressora 3D
for line in gcode:
    # Remova espaços em branco e quebras de linha
    line = line.strip()

    # Ignore linhas de comentário que começam com ";"
    if line.startswith(';'):
        continue

    # Envie a linha para a impressora 3D e aguarde a resposta
    ser.write(line.encode() + b'\n')
    response = ser.readline()

    # Imprima a resposta da impressora 3D
    print(response.decode().strip())

# Fechar a porta serial
ser.close()





