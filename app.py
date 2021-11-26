from flask import Flask

FLASK_APP = Flask(__name__)

@FLASK_APP.route('/')
def index():
    return 'Web App with Python Flask!'

if __name__== "__main__":
    FLASK_APP.run(debug=True, host='0.0.0.0', port=80)