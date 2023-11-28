#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template

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


@app.route('/python')
@app.route('/python/<text>')
def python(text='is cool'):
    """display Python concatenating with any text"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>')
def number(n):
    """display n is a number with a condition"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """display n is a template number with a condition"""
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
