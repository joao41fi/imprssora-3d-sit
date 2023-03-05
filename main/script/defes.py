import serial
import time
import os 

def imprimir(ficheiro):
    
    
    ser  = serial.Serial(os.path.abspath('/dev/ttyACM0'), 250000, timeout=1)
    with open(os.path.abspath(ficheiro), 'r') as f:
     gcode = f.readlines()


    for line in gcode:
    
      line = line.strip()
      print(line)
    
      if line.startswith(';'):
         continue
      ser.write(b"?\n"(line))
      response = ser.readline()

    ser.close()
   


def home():
    ser  = serial.Serial(os.path.abspath('/dev/ttyACM0'), 250000, timeout=1)
    time.sleep(5)  
    ser.write(b"G28\n") 
    ser.close()



    


