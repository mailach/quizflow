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
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')
            json_data = json.loads(decoded_line)
            logging.error(json_data)

    kafka_producer.flush()
    emit('status', {'msg': 'Send create-question event'})
