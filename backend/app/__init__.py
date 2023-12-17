import os
import json
from kafka import KafkaProducer

from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS

from logging.config import dictConfig



dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)

# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate


# db = SQLAlchemy()
# migrate = Migrate()
socketio = SocketIO()
kafka_producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'), 
    key_serializer=lambda v: v.encode('utf-8'))



# PG_PW = os.environ.get("POSTGRES_PASSWORD")
# PG_USER = os.environ.get("POSTGRES_USER")
# PG_DB = os.environ.get("POSTGRES_DB")
# PG_HOST = os.environ.get("POSTGRES_HOST")
# PG_PORT = os.environ.get("POSTGRES_PORT")

# postgres_connection = f"postgresql://{PG_USER}:{PG_PW}@{PG_HOST}:{PG_PORT}/{PG_DB}"

STAGE = os.environ.get("STAGE")
FLASK_SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")


def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    CORS(app)
    # app.config["SQLALCHEMY_DATABASE_URI"] = postgres_connection
    app.config['JSON_AS_ASCII'] = False

    app.secret_key = FLASK_SECRET_KEY
    # db.init_app(app)
    # migrate.init_app(app, db)

    from .participant import participant
    app.register_blueprint(participant)

    from .admin import admin, start_kafka_listener
    app.register_blueprint(admin)
    
    socketio.init_app(app, cors_allowed_origins="*")
    start_kafka_listener(socketio)
    return app

