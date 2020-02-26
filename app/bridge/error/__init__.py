from app.bridge.constants.error import ServerOk, Error


def get_result_bool(error_code):
    if isinstance(error_code, ServerOk):
        return True
    return False


def get_result_msg(error_code):
    if isinstance(error_code, ServerOk):
        return ''
    if isinstance(error_code, Error):
        return error_code.message
    return None


def get_http_status(error_code, method='GET'):
    if isinstance(error_code, ServerOk):
        if method in ['GET', 'PUT']:
            error_code.http_code = 200
        elif method == 'POST':
            error_code.http_code = 201
        elif method == 'DELETE':
            error_code.http_code = 204
    return error_code.http_code


def get_msg_error(error_code, *args, **kwargs):
    return {
        'result': get_result_bool(error_code),
        'message': get_result_msg(error_code),
        'error_code': get_http_status(error_code, *args, **kwargs),
    }
