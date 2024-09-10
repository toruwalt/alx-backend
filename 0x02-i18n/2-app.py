#!/usr/bin/env python3
"""Flask app for i18n"""
import requests
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration class for i18n settings."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
app.url_map.strict_slashes = False


@babel.localeselector
def get_locale():
    """Gets the currect location"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello_world() -> str:
    """Return to the index.html page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    """Runs the app in debug mode"""
    app.run(host='0.0.0.0', port=5000)
