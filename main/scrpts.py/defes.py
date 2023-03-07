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


def get_frame():
    # Carrega a imagem
    img_path = "image.jpg" # Substitua com o caminho para a sua imagem
    img = cv2.imread(img_path)
    
    while True:
        # Codifica a imagem em formato JPEG
        ret, jpeg = cv2.imencode('.jpg', img)
        frame = jpeg.tobytes()
        
        # Retorna o frame para exibir no navegador
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

