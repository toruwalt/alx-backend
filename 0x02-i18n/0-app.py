#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Return to the index.html page"""
    return render_template('index.html')


if __name__ == '__main__':
    """Runs the app in debug mode"""
    app.run(debug=True)
