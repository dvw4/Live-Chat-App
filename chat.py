'''
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)

messages = []

@app.route('/')
def index():
    return render_template('chat1.html')

@socketio.on('send_message')
def handle_message(data):
    user = data['user']
    message = data['message']

    if user and message:
        messages.append({'user': user, 'message': message})
        socketio.emit('new_message', {'user': user, 'message': message}, broadcast=True)

@socketio.on('get_messages')
def handle_get_messages():
    socketio.emit('initial_messages', messages)

if __name__ == '__main__':
     socketio.run(app, debug=True, allow_unsafe_werkzeug=True)


'''
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

messages = []


@app.route('/')
def user1_page():
    return render_template('chat1.html', user='User 1')


@app.route('/user2')
def user2_page():
    return render_template('chat_user2.html', user='User 2')


@socketio.on('send_message')
def handle_send_message(data):
    user = data['user']
    message = data['message']
    messages.append({'user': user, 'message': message})
    socketio.emit('new_message', {'user': user, 'message': message})


@socketio.on('connect')
def handle_connect():
    socketio.emit('initial_messages', messages)


if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
