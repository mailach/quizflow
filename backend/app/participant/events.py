import logging
from flask_socketio import emit
from flask import request
from .. import socketio, kafka_producer



@socketio.on('register', namespace='/register')
def register(message):
    logging.error(message)
    logging.error(request.sid)
    kafka_producer.send("teams", key=message, value={"id": message, "points": 0, "activated": 0, "client_id":request.sid })
    
    emit("waiting", {"giphUrl": "Specific to use", "msg": "Please wait..."}, room=request.sid)






