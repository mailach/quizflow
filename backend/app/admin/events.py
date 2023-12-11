import logging

from flask_socketio import emit
from .. import socketio, producer


@socketio.on('create-question', namespace='/admin')
def test(message):
    logging.error(message)
    producer.send("create-questions", message)
    producer.flush()
    emit('status', {'msg': 'Send create-question event'})
