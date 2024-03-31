import logging
from flask_socketio import emit
from flask import request
from .. import socketio, kafka_producer



@socketio.on('register', namespace='/register')
def get_questions(message):
    logging.error(message)
    print(request.sid)
    kafka_producer.send("teams", key=message, value={"id": message, "points": 0, "activated": 0, "client_id":request.sid })
    emit("registration", {"msg": "Specific to use"}, room=request.sid)

    emit('registration', {"msg": "successful"})






