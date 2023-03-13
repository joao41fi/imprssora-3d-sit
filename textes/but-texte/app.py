from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button', methods=['POST'])
def button():
    button_id = request.form['button_id']
    if button_id == 'E1':
        print(button_id)
        print('Button 1 clicked')
    elif button_id == '2':
        print('Button 2 clicked')
    elif button_id == '3':
        print('Button 3 clicked')
    elif button_id == '4':
        print('Button 4 clicked')
    return render_template('index.html')

if __name__ == '__main__':
    app.run()