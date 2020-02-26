import string
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
    duration_msg = 'Duration must be positive integer'
    assert duration > 0, duration_msg

    # verify board
    if 'board' in payload:
        assert_key(payload, 'board', str)
        board_elems = board.split(', ')
        board_invalid_len_msg = 'Invalid boogle board length'
        
        assert len(board_elems) == 16, 

        board_invalid_element_msg = 'Invalid boogle board string. Must contain only letters or *'
        for elem in board_elems:
            assert elem in allowed_character, board_invalid_element_msg


@request_validator
def validate_update_game_request(payload):
    assert_key(payload, 'id', int)
    assert_key(payload, 'token', str)
    assert_key(payload, 'word', str)
