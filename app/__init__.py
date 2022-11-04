#!/usr/bin/python3
"""
creates an application factory
"""
from os import path, getenv

from flask import Flask
from flask_socketio import SocketIO
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
env_file = path.join(basedir, '..', '.env')
load_dotenv(env_file)
frontend_port = getenv('FRONTEND_PORT')

def create_server():
    """application factory"""
    app = Flask(__name__)
    port = (frontend_port if frontend_port else '5500')
    socketio = SocketIO(app, cors_allowed_origins=[f'http://127.0.0.1:{port}'])

    return socketio, app
