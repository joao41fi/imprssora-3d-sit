import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google
import logging

load_dotenv()
app = Flask(__name__)
client_id = '652183645625-uk4cvnoqmhqa6lao9oki2g5j49gcc2e6.apps.googleusercontent.com'
client_secret = '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'
app.secret_key = "\\\x8eY\xf5\xab=\r.-\xbe\xe3}~\xc7\x19\x05z\xf4\xb5=\xfa\xf4"

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

blueprint = make_google_blueprint(
    client_id=client_id,
    client_secret=client_secret,
    reprompt_consent=True,
    scope=["profile", "email"]
)
app.register_blueprint(blueprint, url_prefix="/login")

@app.route("/")
def index():
    google_data = None
    user_info_endpoint = '/oauth2/v2/userinfo'
    if google.authorized:
        google_data = google.get(user_info_endpoint).json()
    print(google_data)
    return render_template('index.j2',
                           google_data=google_data,
                           fetch_url=google.base_url + user_info_endpoint)

@app.route('/login')
def login():
    return redirect(url_for('google.login'))


if __name__ == '__main__':
 app.run(debug=True,host='0.0.0.0')