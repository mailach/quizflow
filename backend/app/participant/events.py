import logging
from flask_socketio import emit
from .. import socketio, kafka_producer



@socketio.on('register', namespace='/register')
def get_questions(message):
    logging.error(message)
    emit('registration', {"msg": "successful"})






