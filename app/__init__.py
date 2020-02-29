# Import library
import os
import logging

from flask import Flask, jsonify
from flask_mongoengine import MongoEngine
from werkzeug.exceptions import HTTPException
from logging.handlers import TimedRotatingFileHandler


# Define the WSGI application object
flask_app = Flask(__name__)

# Configurations
flask_app.config.from_object('config.flask_config')

# MongoDB database connection
db = MongoEngine(flask_app)

# Define the database object which is imported
# by modules and controllers
unit_test_mode = os.environ.get('UNIT_TEST_MODE', False)


def setup_db():
    # Import DB models here ...
    from app.game.models.board_model import Board
    from app.game.models.corpus_model import Corpus
    from app.game.models.game_model import Game

    # setup default corpus
    from app.game.data_access.corpus_model_manager import get_or_create_corpus
    get_or_create_corpus(
        corpus_name=flask_app.config['DEFAULT_CORPUS_NAME'],
        corpus_path=flask_app.config['DEFAULT_CORPUS_PATH']
    )


def setup_logging():
    if not os.path.isdir('logs'):
        os.makedirs('logs')

    formatter = logging.Formatter('[%(asctime)s] %(message)s')

    handler_info = TimedRotatingFileHandler('./logs/info.log', when='midnight', interval=1, backupCount=5)
    handler_info.setLevel(logging.INFO)
    handler_info.setFormatter(formatter)

    handler_error = TimedRotatingFileHandler('./logs/error.log', when='midnight', interval=1, backupCount=5)
    handler_error.setLevel(logging.ERROR)
    handler_error.setFormatter(formatter)

    # access log
    logger = logging.getLogger('werkzeug')
    handler_access = logging.FileHandler('./logs/access.log')

    flask_app.logger.addHandler(handler_info)
    flask_app.logger.addHandler(handler_error)
    logger.addHandler(handler_access)

    def handle_default_error(e):
        flask_app.logger.exception(e)

    flask_app.register_error_handler(Exception, handle_default_error)


def get_register_blueprints():
    # Import Blueprints here ...
    from app.game.views.game_views import mod_game

    return [
        mod_game,
    ]


"""
Setup all the methods for Flask App
WARNING: ORDER IS IMPORTANT !!!
"""


"""
DEFINE DB
"""
setup_db()


"""
BLUEPRINT REGISTER
"""

[flask_app.register_blueprint(blueprint) 
for blueprint in get_register_blueprints()]

if not unit_test_mode:
    # disable file logging for the unit test
    setup_logging()


"""
ERROR HANDLER FOR HTTP ERROR
"""