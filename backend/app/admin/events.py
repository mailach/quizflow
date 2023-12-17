import logging
from flask_socketio import emit
from .. import socketio, kafka_producer
from ..ksql import query_ksql




@socketio.on('get-questions', namespace='/admin')
def get_questions():
    emit('questions', {'questions': query_ksql("Select * from QUESTIONS_TABLE;")})
    logging.info("Questions emitted")

@socketio.on('create-question', namespace='/admin')
def create_question(message):
    logging.info("Save question %r", message)
    key = message['id']
    kafka_producer.send("create-questions", key=key, value=message)
    kafka_producer.flush()
