import logging
import json

from flask_socketio import emit
from .. import socketio, kafka_producer
from ..ksql import query_ksql


@socketio.on('create-question', namespace='/admin')
def test(message):
    logging.error(message)
    key = message['id']
    kafka_producer.send("create-questions", key=key, value=message)

    response = query_ksql("Select * from QUESTIONS_TABLE;")
    logging.error(response)

    kafka_producer.flush()
    emit('status', {'msg': 'Send create-question event'})
