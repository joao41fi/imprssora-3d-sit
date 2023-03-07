import serial
import time
import os 
import sys
import fileinput
import cv2 

def home():
    ser  = serial.Serial(os.path.abspath('/dev/ttyACM0'), 250000, timeout=1)
    time.sleep(5)  
    ser.write(b"G28\n") 
    ser.close()


# Define o nome do arquivo
def caminho(new_line,old_line ):

 filename = '/home/joao41/Desktop/imprssora-3d-sit/main/scrpts.py/texte.cfg'
 
 # Substitui a linha antiga pela nova em todo o arquivo
 for line in fileinput.input(filename, inplace=True):
     if line.strip() == old_line:
         line = new_line + '\n'
     print(line, end='')

def get_image_data():
    while True:
        # Aqui você pode colocar a lógica para gerar os dados da imagem
        yield open('imagem.png', 'rb').read()
        time.sleep(1)