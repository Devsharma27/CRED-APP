from flask import Flask

from logging.config import fileConfig

app = Flask(__name__)

fileConfig('logging.cfg')

@app.route('/')
def hello_world():
    app.logger.info('Processing default request')
    return 'Hello World!'
if __name__== "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
