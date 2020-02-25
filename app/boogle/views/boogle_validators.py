import string
from app.bridge.error import InvalidRequestError
from app.bridge.decorators.validator import (
    request_validator,
    assert_key,
    assert_length
)

allowed_character = set(string.ascii_uppercase + '*')


@request_validator
def validate_create_game_request(payload):
    assert_key(payload, 'id', int)
    assert_key(payload, 'random', bool)

    # verify duration
    assert_key(payload, 'duration', int)
    assert duration > 0 or InvalidRequestError('Duration must be positive integer')

    # verify board
    if 'board' in payload:
        assert_key(payload, 'board', str)
        board_elems = board.split(', ')

        assert len(board_elems) == 16 or \
            InvalidRequestError('Invalid boogle board length')

        for elem in board_elems:
            assert elem in allowed_character or \
                InvalidRequestError('Invalid boogle board string. Must contain only letters or *')


@request_validator
def validate_update_game_request(payload):
    assert_key(payload, 'id', int)
    assert_key(payload, 'token', str)
    assert_key(payload, 'word', str)
