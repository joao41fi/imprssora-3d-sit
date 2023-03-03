
import serial
import time

# Configure a porta serial com as configurações adequadas para a impressora 3D
ser = serial.Serial('/dev/ttyACM0', 250000, timeout=1)

# Enviar alguns comandos para a impressora 3D
time.sleep(5)
ser.write(b"G28\n")  # Home all axes
time.sleep(5)  # Espera 5 segundos
ser.write(b"G1 X10 Y10 Z10 F500\n")  # Move to position (10, 10, 10) at speed 500

# Fechar a porta serial
ser.close()
