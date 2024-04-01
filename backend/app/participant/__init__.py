

from flask import Blueprint


participant = Blueprint('participant', __name__)



from . import routes, events

from .kafka_consumer import TeamsConsumerThread
import threading


def start_kafka_participant_listener(socketio):
    teams_consumer = TeamsConsumerThread(socketio)
    teams_thread = threading.Thread(target=teams_consumer.listen)
    teams_thread.start()
