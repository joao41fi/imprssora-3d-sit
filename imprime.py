import serial
import time

# Configure a porta serial com as configurações adequadas para a impressora 3D
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

# Defina a taxa de transmissão para 250000 baud
ser.baudrate = 250000

# Abra o arquivo G-code e leia seu conteúdo
with open('/home/joao41/Desktop/imprssora-3d-sit/arquivo.gcode', 'r') as f:
    gcode = f.readlines()

# Configure um buffer de impressão
BUFFER_SIZE = 128
buffer = []

# Envie cada linha do arquivo G-code para a impressora 3D
for line in gcode:
    # Remova espaços em branco e quebras de linha
    line = line.strip()

    # Ignore linhas de comentário que começam com ";"
    if line.startswith(';'):
        continue

    # Adicione a linha ao buffer de impressão
    buffer.append(line)

    # Se o buffer estiver cheio, envie seu conteúdo para a impressora 3D
    if len(buffer) >= BUFFER_SIZE:
        # Envie o conteúdo do buffer para a impressora 3D e aguarde a resposta
        ser.write('\n'.join(buffer).encode() + b'\n')
        response = ser.readline()

        # Imprima a resposta da impressora 3D
        print(response.decode().strip())

        # Limpe o buffer de impressão
        buffer = []

# Envie o conteúdo restante do buffer para a impressora 3D
if len(buffer) > 0:
    # Envie o conteúdo do buffer para a impressora 3D e aguarde a resposta
    ser.write('\n'.join(buffer).encode() + b'\n')
    response = ser.readline()

    # Imprima a resposta da impressora 3D
    print(response.decode().strip())

# Fechar a porta serial
ser.close()

