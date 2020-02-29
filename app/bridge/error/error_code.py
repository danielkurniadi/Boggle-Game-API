"""
DEFINITION OF ERROR CODE
"""

from .base_code import BaseCode


class ServerOk(BaseCode):
    error_code = 0

    def __init__(self, method='GET'):
        if method in ['GET', 'PUT']:
            self.http_code = 200
        elif method == 'POST':
            self.http_code = 201
        elif method == 'DELETE':
            self.http_code = 204

    def get_result_bool(self):
        return True

    def get_result_msg(self):
        return 'Success'


class Error(BaseCode):
    message = ''
    error_code = 1
    http_code = 400

    def __init__(self, message):
        self.message = message

    def get_result_bool(self):
        return False

    def get_result_msg(self):
        return self.message


class ResourceNotFound(Error):
    error_code = 2
    http_code = 404


class OperationNotSupported(Error):
    error_code = 3
    http_code = 400


class InvalidRequest(Error):
    error_code = 4
    http_code = 400


class DatabaseError(Error):
    error_code = 5
    http_code = 500
