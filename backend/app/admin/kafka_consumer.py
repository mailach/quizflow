# kafka_consumer.py within your admin blueprint directory
import logging
from kafka import KafkaConsumer
from ..ksql import query_ksql

class QuestionConsumerThread:
    def __init__(self, socketio):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.consumer = KafkaConsumer(
            'question-table',
            bootstrap_servers=['kafka:9092'])
        self.socketio = socketio
        logging.info("CONSUMER CREATED")

    def listen(self):
        self.logger.info("Kafka Consumer started listening...")
        for message in self.consumer:
            self.logger.info("Consumer received messages %r...", message)
            topic = message.topic
            self.logger.info("Consumer received topic %r...", topic)
            if topic == 'question-table':
                self.logger.info("Emitting questions...")
                self.socketio.emit('questions', {'questions': [q for q in query_ksql("Select * from QUESTIONS_TABLE;") if q["deleted"]==0]}, namespace="/admin")
            elif topic == 'round-table':
                logging.error(topic)
                self.socketio.emit('rounds', {'rounds': query_ksql("Select * from ROUNDS_TABLE;")}, namespace="/admin")

class RoundConsumerThread:
    def __init__(self, socketio):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.consumer = KafkaConsumer(
            'round-table',
            bootstrap_servers=['kafka:9092'])
        self.socketio = socketio
        logging.info("CONSUMER CREATED")

    def listen(self):
        self.logger.info("Kafka Consumer started listening...")
        for message in self.consumer:
            self.logger.info("Consumer received messages %r...", message)
            topic = message.topic
            self.logger.info("Consumer received topic %r...", topic)
            if topic == 'question-table':
                self.logger.info("Emitting questions...")
                self.socketio.emit('questions', {'questions': [q for q in query_ksql("Select * from QUESTIONS_TABLE;") if q["deleted"]==0]}, namespace="/admin")
            elif topic == 'round-table':
                logging.error(topic)
                self.socketio.emit('rounds', {'rounds': query_ksql("Select * from ROUNDS_TABLE;")}, namespace="/admin")
            




class TeamsConsumerThread:
    def __init__(self, socketio):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.consumer = KafkaConsumer(
            'teams-table',
            bootstrap_servers=['kafka:9092'])
        self.socketio = socketio
        logging.info("CONSUMER CREATED")

    def listen(self):
        self.logger.info("Kafka Consumer started listening...")
        for message in self.consumer:
            self.logger.info("Consumer received messages %r...", message)
            topic = message.topic
            self.logger.info("Consumer received topic %r...", topic)
            if topic == 'teams-table':
                logging.error(topic)
                self.socketio.emit('teams', {'teams': query_ksql("Select * from TEAMS_TABLE;")}, namespace="/admin")