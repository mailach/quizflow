import logging
import json

from flask_socketio import emit
from .. import socketio, kafka_producer
from ..ksql import query_ksql


@socketio.on('get-questions', namespace='/admin')
def get_questions(message):
    logging.error("jaaaaaaaa")
    logging.error(message)
    emit('questions', {'questions': query_ksql("Select * from QUESTIONS_TABLE;")})

@socketio.on('create-question', namespace='/admin')
def create_question(message):
    logging.error(message)
    key = message['id']
    kafka_producer.send("create-questions", key=key, value=message)

    kafka_producer.flush()
    emit('status', {'msg': 'Send create-question event'})
