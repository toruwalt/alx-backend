#!/usr/bin/env python3
"""Flask app for i18n"""
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """Return to the index.html page"""
    return render_template('index.html')


if __name__ == '__main__':
    """Runs the app in debug mode"""
    app.run(host='0.0.0.0', port=5000)
