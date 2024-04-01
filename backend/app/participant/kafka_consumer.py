# kafka_consumer.py within your admin blueprint directory
import logging
import json
from kafka import KafkaConsumer

class TeamsConsumerThread:
    def __init__(self, socketio):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.consumer = KafkaConsumer(
            'teams-table',
            bootstrap_servers=['kafka:9092'], 
            value_deserializer=lambda m: json.loads(m.decode('ascii')))
        self.socketio = socketio
        logging.info("CONSUMER CREATED")

    def listen(self):
        self.logger.info("Kafka Consumer started listening...")
        for message in self.consumer:
            self.logger.info("Consumer received messages %r...", message)
            topic = message.topic
            self.logger.info("Consumer received topic %r...", topic)
            if topic == 'teams-table':
                self.logger.info("Teams changed...")
                self.logger.info(message.value)
                if message.value["ACTIVATED"]==1:
                    logging.error(message.value)
                    self.socketio.emit('activation',{"name": "test"}, namespace="/register", room=message.value["CLIENT_ID"])

