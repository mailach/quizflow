from flask_socketio import emit
from .. import socketio


@socketio.on('test', namespace='/')
def test(message):
    emit('status', {'msg': 'Yep, test successful'})



