import serial
import time
import os 

def imprimir(ficheiro):
    
    print(os.getcwd())
    #ser = serial.Serial(os.chdir('/dev/ttyACM0'), 250000, timeout=1)
    ser  = serial.Serial(os.path.abspath('/dev/ttyACM0'), 250000, timeout=1)
    with open(os.chdir(os.path.abspath(ficheiro)), 'r') as f:
     gcode = f.readlines()


    for line in gcode:
    
     line = line.strip()

    
     if line.startswith(';'):
        continue
     ser.write(line.encode() + b'\n')
     response = ser.readline()

    ser.close()
   
