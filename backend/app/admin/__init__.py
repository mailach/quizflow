from flask import Blueprint

from .routes import admin
from . import events

# __init__.py of your admin blueprint

from .kafka_consumer import QuestionConsumerThread, RoundConsumerThread
import threading

admin_blueprint = Blueprint('admin', __name__)

# Import routes, etc.

def start_kafka_listener(socketio):
    question_consumer = QuestionConsumerThread(socketio)
    question_thread = threading.Thread(target=question_consumer.listen)
    question_thread.start()

    round_consumer = RoundConsumerThread(socketio)
    round_thread = threading.Thread(target=round_consumer.listen)
    round_thread.start()

