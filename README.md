# Basic Chat App
A basic text chat app using websockets

Uses [flaskSocketIO](https://flask-socketio.readthedocs.io/) on the backend and [socket.io](https://socket.io/) JS library on the frontend (vanilla JS)

To run:
- Install dependencies using `pipenv install`. Be sure to have [pipenv](https://pipenv.pypa.io/en/latest/) install
- Set the FLASK_SECRET_KEY (and other) env variables in a .env file. They are loaded automatically with in the app factory using python-dotenv.
- Set the frontend port using the FRONTEND_PORT env variable. Default is 5500. This is important for the CORS policy of the server.
- Start the flaskSocketIO server by running `python3 -m wsgi` from project root dir. By default, it runs on localhost on port 5000. You can set a port and host using the `HOST` and `PORT` env variables. However, you will have to change the backend port in `index.js`
- Serve the frontend on port 5500 or the frontend port you specified earlier.
- Open the app on separate browser tabs/windows
- Enter text and enjoy!  

This is just a brief test to see the library features.