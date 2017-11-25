from flask import Flask

app = Flask(__name__)
PORT = 8000
DEBUG = True

@app.errorhandler(400)
def not_found(error):
    return "Not Found."

@app.route('/', methods=['GET'])
def index():
    return "Hello World."

if __name__== '__main__':
    app.run(port=PORT, debug=DEBUG)
