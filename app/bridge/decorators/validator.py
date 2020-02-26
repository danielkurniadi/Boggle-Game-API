import inspect
from functools import wraps
from flask import jsonify, request

from app import flask_app
from app.bridge.error.error_code import InvalidRequest


def request_validator(validator):
    """
    Decorator that will convert normal function into input validation decorator to validate request.
    The resulting validator function is only appropriate to be used in views function only.
    :type: validator: function
    :rtype: function
    """
    def __func(func):
        @wraps(func)
        def _func(*args, **kwargs):
            try:
                param = {}
                validator_args = inspect.getfullargspec(validator).args
                if 'payload' in validator_args:
                    param.update(payload = request.json or {})
                if 'query' in validator_args:
                    param.update(query = request.args or {})
                validator(**param)

            except AssertionError as e:
                flask_app.logger.error(
                    'validation error: `%s` | request: `%s`',
                    str(e), str(request)
                )
                return jsonify(InvalidRequest(str(e)).to_dict())

            return func(*args, **kwargs)

        return _func
    return __func


def assert_key(data, key, var_type, optional=False):
    """ 
    Check whether key is in data and it is in the correct data type.
    May allow the key to not be in the data if optional is True
    :type: data: dict
    :type: key: string
    :type: var_type: type
    :type: optional: bool
    """
    if optional is True and key not in data:
        return

    if not isinstance(data, list):
        key_required_msg = 'field `%s` is required' % key
        assert (key in data), key_required_msg

    type_error_msg = 'field `%s` expected to be `%s` but received `%s`' % (
        key, var_type, type(data[key]))

    if isinstance(var_type, list):
        assert (type(data[key]) in var_type), type_error_msg
    else:
        assert isinstance(data[key], var_type), type_error_msg


def assert_length(data, key, length):
    """ 
    Check whether key is in data and it is in exact correct length
    :type: data: dict
    :type: key: string
    :type: var_type: type
    """
    key_required_msg = 'field `%s` is required' % key
    assert (key in data), key_required_msg

    length_error_msg = (
        'field `%s` expected to be'
        '`%s` length but received `%s`'
        % (key, length, len(data[key]))
    )
    assert (len(data[key]) == length), length_error_msg
