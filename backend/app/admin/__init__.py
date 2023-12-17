from flask import Blueprint

from .routes import admin
from . import events

# __init__.py of your admin blueprint

from .kafka_consumer import KafkaConsumerThread
import threading

admin_blueprint = Blueprint('admin', __name__)

# Import routes, etc.

def start_kafka_listener(socketio):
    kafka_listener = KafkaConsumerThread(socketio)
    kafka_thread = threading.Thread(target=kafka_listener.listen)
    kafka_thread.start()

