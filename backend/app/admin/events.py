import logging
from flask_socketio import emit
from .. import socketio


@socketio.on('create-question', namespace='/admin')
def test(message):
    logging.error(message)
    emit('status', {'msg': 'Yep, admin test successful'})



