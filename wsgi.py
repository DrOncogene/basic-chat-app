#!/usr/bin/python3
"""
instantiate the app from the app factory
"""
from os import environ as env
from flask_socketio import emit

from app import create_server

socketio, app = create_server()

if __name__ == '__main__':
    PORT = env.get('PORT') if env.get('PORT') else 5000
    HOST = env.get('HOST') if env.get('HOST') else 'localhost'

    @socketio.on('chat', namespace='/chat')
    def handle_chat(msg):
        """handles the chat event"""
        emit('chat', msg, broadcast=True, include_self=False)
        print(msg)

    socketio.run(app, host=HOST, port=PORT)
