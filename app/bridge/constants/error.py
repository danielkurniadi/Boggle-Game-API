class ServerOk:
    error_code = 0
    http_code = 200


class Error:
    message = ''
    error_code = 1
    http_code = 400

    def __init__(self, message):
        self.message = message


class DatabaseError(Error):
    error_code = 2
    http_code = 404


class OperationNotSupported(Error):
    error_code = 3
    http_code = 400


class InvalidRequest(Error):
    error_code = 4
    http_code = 400
