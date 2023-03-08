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

def comandos(comand):
    ser  = serial.Serial(os.path.abspath('/dev/ttyACM0'), 250000, timeout=1)
    time.sleep(5)  
    ser.write(b""comand) 
    ser.close()


# Define o nome do arquivo
def caminho(numero_linha, nova_linha ):

 filename = '/home/joao41/Desktop/imprssora-3d-sit/main/scrpts.py/texte.cfg'

 with open(filename, 'r') as file:
        linhas = file.readlines()
 with open(filename, 'w') as file:
        for indice, linha in enumerate(linhas):
            if (indice == numero_linha - 1):
                file.write(nova_linha + '\n')
            else:
                file.write(linha)