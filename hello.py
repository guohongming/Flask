__author__ = 'Guo'
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello World!'

if __name__ == '__main__':
    app.run(debug=True)