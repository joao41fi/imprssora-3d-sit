from flask import Flask, render_template, Response
import cv2 # pip install opencv-python

app = Flask(__name__)

# cria uma instância para a captura de vídeo
cap = cv2.VideoCapture(0)

# função para obter o feed de vídeo da câmera
def get_frame():
    while True:
        # lê um quadro da câmera
        ret, frame = cap.read()

        # converte o quadro para um objeto de fluxo de bytes
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # retorna o quadro como uma resposta de streaming
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# rota para renderizar a página com o feed de vídeo da câmera
@app.route('/')
def index():
    return render_template('index.html')

# rota para transmitir o feed de vídeo da câmera como uma resposta de streaming
@app.route('/video_feed')
def video_feed():
    return Response(get_frame(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# inicia o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True)
#