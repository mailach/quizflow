import logging
from flask_socketio import emit
from .. import socketio, kafka_producer
from ..ksql import query_ksql




@socketio.on('get-questions', namespace='/admin')
def get_questions():
    emit('questions', {'questions': [q for q in query_ksql("Select * from QUESTIONS_TABLE;") if q["deleted"]==0]})
    logging.info(query_ksql("Select * from QUESTIONS_TABLE;"))
    logging.info("Questions emitted")

@socketio.on('get-rounds', namespace='/admin')
def get_rounds():
    emit('rounds', {'rounds': query_ksql("Select * from ROUNDS_TABLE;")}, namespace="/admin")
    logging.info("Rounds emitted")


@socketio.on('get-teams', namespace='/admin')
def get_teams():
    emit('teams', {'teams': query_ksql("Select * from TEAMS_TABLE;")}, namespace="/admin")
    logging.info("Teams emitted")


@socketio.on('create-question', namespace='/admin')
def create_question(message):
    logging.info("Save question %r", message)
    message["deleted"]=0
    key = message['id']
    kafka_producer.send("question", key=key, value=message)
    kafka_producer.flush()

@socketio.on('create-round', namespace='/admin')
def create_round(message):
    logging.info("Save round %r", message)
    key = message['id']
    kafka_producer.send("create-round", key=key, value=message)
    kafka_producer.flush()


@socketio.on('delete-question', namespace='/admin')
def delete_question(message):
    logging.info("Delete question %r", message)

    message["deleted"]=1
    key = message['id']
    kafka_producer.send("question", key=key, value=message)
    kafka_producer.flush()


@socketio.on('activate-team', namespace='/admin')
def activateTeam(team):
    logging.info("Delete question %r", team)
    kafka_producer.send("teams", key=team["id"], value={"id": team["id"], "activated": 1})
    kafka_producer.flush()