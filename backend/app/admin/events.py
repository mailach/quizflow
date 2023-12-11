from flask_socketio import emit
from .. import socketio


@socketio.on('test', namespace='/admin')
def test(message):
    emit('status', {'msg': 'Yep, admin test successful'})



