from app.bridge.error.error_code import (
    ServerOk,
    DatabaseError,
    OperationNotSupported,
)


def get_boogle_game(game_id):
    data = {
        'id': 1,
        'token': '9dda26ec7e476fb337cb158e7d31ac6c', 
        'duration': 600, 
        'board': 'A, C, E, D, L, U, G, *, E, *, H, T, G, A, F, K',
        'time_left': 30,
        'points': 10
    }
    error_code = ServerOk(method='GET')
    return  error_code, data


def update_boogle_game(game_id, token, word):
    data = {
        "id": 1,
        "token": "9dda26ec7e476fb337cb158e7d31ac6c",
        "duration": 12345,
        "board": "A, C, E, D, L, U, G, *, E, *, H, T, G, A, F, K",
        "time_left": 10000,
        "points": 10
    }
    error_code = ServerOk(method='PUT')
    return error_code, data


def create_boogle_game(duration, random, board):
    data = {
        "id": 1,
        "token": "9dda26ec7e476fb337cb158e7d31ac6c",
        "duration": 12345,
        "board": "A, C, E, D, L, U, G, *, E, *, H, T, G, A, F, K"
    }
    error_code = ServerOk(method='POST')
    return error_code, data
