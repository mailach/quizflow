

from flask import Blueprint


participant = Blueprint('participant', __name__)



from . import routes, events

from .kafka_consumer import TeamsConsumerThread, LiveConsumerThread
import threading


def start_kafka_participant_listener(socketio):
    teams_consumer = TeamsConsumerThread(socketio)
    teams_thread = threading.Thread(target=teams_consumer.listen)
    teams_thread.start()


    live_consumer = LiveConsumerThread(socketio)
    live_thread = threading.Thread(target=live_consumer.listen)
    live_thread.start()
