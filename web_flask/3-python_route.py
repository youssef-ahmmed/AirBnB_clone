#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """display hello holberton"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """display holberton"""
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    """display C concatenating with any text"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/<text>')
@app.route('/python', defaults={'text': 'is cool'})
def python(text):
    """display Python concatenating with any text"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
