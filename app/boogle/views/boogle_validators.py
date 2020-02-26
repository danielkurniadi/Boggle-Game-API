import string
from app.bridge.decorators.validator import (
    request_validator,
    assert_key,
    assert_length
)


ALLOWED_CHARACTERS = set(string.ascii_uppercase + '*')

INVALID_DURATION_MSG = 'Duration must be positive integer'

INVALID_BOARD_MSG = ('Invalid input for 4x4 boogle board. '
                     'Must contain exactly 16 characters in comma seperated '
                     'and contain letters or * only')


@request_validator
def validate_create_game_request(payload):
    assert_key(payload, 'random', bool)

    # verify duration
    assert_key(payload, 'duration', int)
    assert payload['duration'] > 0, INVALID_DURATION_MSG

    # verify board
    if 'board' in payload:
        assert_key(payload, 'board', str)
        board_elems = payload['board'].replace(' ', '').split(',')
        board_invalid_len_msg = 'Invalid boogle board length'

        assert len(board_elems) == 16, INVALID_BOARD_MSG

        for elem in board_elems:
            assert elem in ALLOWED_CHARACTERS, INVALID_BOARD_MSG


@request_validator
def validate_update_game_request(payload):
    assert_key(payload, 'token', str)
    assert_key(payload, 'word', str)
