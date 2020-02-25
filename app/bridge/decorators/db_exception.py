from functools import wraps
from app import flask_app
from app.bridge.constants.error import ServerOk, DatabaseError


def db_exception(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            flask_app.logger.error('function: %s| error: %s', f, e)
            return DatabaseError(str(e))

    return wrapped
