import os

from flask import Flask, render_template, request, redirect, session, url_for
from flask_cors import CORS
from flask_talisman import Talisman

from backend import request_functions

# App setup
app = Flask(__name__)
CORS(app)
### Set app secret
app.secret_key = os.environ['app_secret']
### Set content security policy and enable Talisman
SELF = "'self'"
talisman = Talisman(
    app,
    content_security_policy={
        'default-src': [SELF, '*.gstatic.com', '*.fontawesome.com',
                        '*.jsdelivr.net', '*.googleapis.com', '*.spotify.com'],
    },
    content_security_policy_nonce_in=['script-src'],
    feature_policy={
        'geolocation': '\'none\'',
    }
)


@app.route('/create-playlist/tempo=<tempo>&energy=<energy>', methods=['GET', 'POST'])
def playlist_creation(tempo, energy):
    auth_header = request.headers['Authorization']
    auth_header = {"Authorization": auth_header}
    print(auth_header)
    complete_playlist_data = request_functions.get_complete_playlist(auth_header, [energy, tempo])
    print(complete_playlist_data)
    return complete_playlist_data


if __name__ == '__main__':
    app.run()
