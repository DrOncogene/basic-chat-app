#!/usr/bin/python3
"""
creates an application factory
"""
from os import path

from flask import Flask
from flask_socketio import SocketIO
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
env_file = path.join(basedir, '..', '.env')
load_dotenv(env_file)

def create_server():
    """application factory"""
    app = Flask(__name__)
    socketio = SocketIO(app, cors_allowed_origins=['http://127.0.0.1:5500'])

    return socketio, app
