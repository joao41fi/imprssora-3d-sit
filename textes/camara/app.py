from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# função para obter o feed de vídeo da câmera
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

# rota para renderizar a página com o feed de vídeo da câmera
@app.route('/')
def index():
    return render_template('index.html')

# rota para transmitir o feed de vídeo da câmera como uma resposta de streaming
@app.route('/video_feed')
def video_feed():
    return Response(get_frame(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')




if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

