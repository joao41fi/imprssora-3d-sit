import serial
import time
import os 
import sys
meus_modulos_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'db'))
sys.path.insert(0, meus_modulos_dir)

from  ler_tabela import *
from atualizar import *
def imprimir(ficheiro):
    
    
    ser  = serial.Serial(os.path.abspath('/dev/ttyACM0'), 250000, timeout=1)
    time.sleep(2)
    
    with open(os.path.abspath(ficheiro), 'r') as f:
     gcode = f.readlines()

    
    for line in gcode:
    
     line = line.strip()
     #print(line)
    
     if line.startswith(';'):
        continue
     ser.write(line.encode() + b'\n')
     response = ser.readline()
     #print(response)

    ser.close()
   


def home():
    ser  = serial.Serial(os.path.abspath('/dev/ttyACM0'), 250000, timeout=1)
    time.sleep(5)  
    ser.write(b"G28\n") 
    ser.close()



    


if __name__ == '__main__':
 ficheiro =abrir('/home/joao41/Desktop/imprssora-3d-sit/main/ficheiro.db','fichieros')
 imprimir('/home/joao41/Desktop/imprssora-3d-sit/arquivo.gcode')
