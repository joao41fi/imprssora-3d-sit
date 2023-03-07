import serial
import time
import os 
import sys
import fileinput
import cv2 
cap = cv2.VideoCapture(0)

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
    camera = cv2.VideoCapture(0)
    while True:
        # lê um quadro da câmera
        ret, frame = camera.read()

        # converte o quadro para um objeto de fluxo de bytes
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # retorna o quadro como uma resposta de streaming
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    # libera o objeto de captura da câmera
    camera.release()
