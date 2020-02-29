from functools import wraps
from mongoengine import errors as mongod_error

from app import flask_app
from app.bridge.error.error_code import (
    ServerOk, Error, ResourceNotFound,
    DatabaseError, OperationNotSupported,
)

def db_exception(f):
    @wraps(f)
    def wrapped(*args, full=False, **kwargs):
        try:
            result = f(*args, **kwargs)

            if isinstance(result, Error):
                return result

            elif result is None:
                return ResourceNotFound('Resource Not Found.')

            return result.to_json(full=full)

        except (mongod_error.NotUniqueError, mongod_error.ValidationError) as e:
            flask_app.logger.error('function: %s| error: %s', f, e)
            return OperationNotSupported(str(e))

        except Exception as e:
            flask_app.logger.error('function: %s| error: %s', f, e)
            return DatabaseError(str(e))

    return wrapped
