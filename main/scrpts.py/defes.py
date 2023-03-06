import serial
import time
import os 
import sys
import fileinput


def home():
    ser  = serial.Serial(os.path.abspath('/dev/ttyACM0'), 250000, timeout=1)
    time.sleep(5)  
    ser.write(b"G28\n") 
    ser.close()


# Define o nome do arquivo
def caminho(new_line,old_line ):
 print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
 filename = '/home/joao41/Desktop/imprssora-3d-sit/main/scrpts.py/texte.cfg'
 print(filename)
 # Substitui a linha antiga pela nova em todo o arquivo
 for line in fileinput.input(filename, inplace=True):
     if line.strip() == old_line:
         line = new_line + '\n'
     print(line, end='')


