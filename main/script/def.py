import serial
import time

def imprimir(ficheiro):

    ser = serial.Serial('../dev/ttyACM0', 250000, timeout=1)
    with open('../home/joao41/Desktop/imprssora-3d-sit/arquivo.gcode', 'r') as f:
     gcode = f.readlines()


    for line in gcode:
    
     line = line.strip()

    
     if line.startswith(';'):
        continue
     ser.write(line.encode() + b'\n')
     response = ser.readline()

    ser.close()
   
