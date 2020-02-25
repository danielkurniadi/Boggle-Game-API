# Import library
import os
import logging
import redis

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
from logging.handlers import TimedRotatingFileHandler


# Define the WSGI application object
flask_app = Flask(__name__)

# Configurations
flask_app.config.from_object('config.flask_config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(flask_app)
unit_test_mode = os.environ.get('UNIT_TEST_MODE', False)


def setup_db():
    # Import DB models here ...
    db.create_all()


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
    return []


"""
set up all the method for the Flask App
WARNING: ORDER IS IMPORTANT !!!
"""

"""
# DEFINE REDIS
"""


def make_redis():
    r = redis.Redis(
        host=flask_app.config['REDIS_HOST'],
        port=flask_app.config['REDIS_PORT'],
        db=flask_app.config['REDIS_DB'],
        password=flask_app.config['REDIS_PASSWORD'],
    )
    return r


flask_app.redis_cache = make_redis()


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
    # disable logging for the unit test
    setup_logging()


"""
ERROR HANDLER FOR BUSINESS LOGIC
"""


@flask_app.errorhandler(AccountInvalidToken)
def account_invalid_token_func(error):
    return jsonify({
        'result': False,
        # 'error_code': ACCOUNT_TOKEN_INVALID,
        # 'error_message': ACCOUNT_TOKEN_INVALID_MESSAGE,
    })


"""
ERROR HANDLER FOR HTTP ERROR
"""


@flask_app.errorhandler(HTTPException)
def http_error(e):
    flask_app.logger.error('http_error|{}'.format(e))
    return jsonify({
        'result': False,
        'error_name': e.name,
        'error_message': e.description,
        'error_code': e.code
    }), e.code
