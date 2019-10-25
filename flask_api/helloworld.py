from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World!"


@app.route('/user/<string:username>')
def hello_world(username=None):
    return "Hello {}!".format(username)


if __name__ == '__main__':
    app.run(debug=True)