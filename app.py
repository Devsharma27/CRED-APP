from flask import Flask
import logging

app = Flask(__name__)
logging.basicConfig(level = logging.INFO, filename='dev.log')
@app.route('/')
def hello():
    return 'hello world Dev!'
if __name__== "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
