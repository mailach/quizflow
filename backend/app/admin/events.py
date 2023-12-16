import logging

from flask_socketio import emit
from .. import socketio, producer


@socketio.on('create-question', namespace='/admin')
def test(message):
    logging.error(message)
    key = message['id']
    producer.send("create-questions", key=key, value=message)

    producer.flush()
    emit('status', {'msg': 'Send create-question event'})
