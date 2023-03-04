import serial
import time
import os 

def imprimir(ficheiro):

    ser = serial.Serial(os.chdir('/dev/ttyACM0'), 250000, timeout=1)
    with open(os.chdir('/home/joao41/Desktop/imprssora-3d-sit/main/'+ficheiro), 'r') as f:
     gcode = f.readlines()


    for line in gcode:
    
     line = line.strip()

    
     if line.startswith(';'):
        continue
     ser.write(line.encode() + b'\n')
     response = ser.readline()

    ser.close()
   
