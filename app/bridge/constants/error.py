class ServerOk:
    error_code = 0


class Error:
    message = ''
    error_code = 1

    def __init__(self, message):
        self.message = message


class DatabaseError(Error):
    error_code = 2


class OperationNotSupported(Error):
    error_code = 3


class InvalidRequest(Error):
    error_code = 99
