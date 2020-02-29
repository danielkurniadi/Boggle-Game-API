from app import flask_app
from app.bridge.managers import token_manager
from app.game.data_access import (
    corpus_model_manager,
    board_model_manager,
    game_model_manager
)
from app.bridge.error.error_code import (
    ServerOk,
    ResourceNotFound,
    DatabaseError,
    OperationNotSupported,
)

DEFAULT_CORPUS_NAME = flask_app.config['DEFAULT_CORPUS_NAME']
DEFAULT_CORPUS_PATH = flask_app.config['DEFAULT_CORPUS_PATH']


# ------------------------------
# GAME MANAGER
# ------------------------------

def get_boggle_game(game_id):
    game_json = game_model_manager.get_game_by_id(game_id, full=True)
    if isinstance(game_json, (ResourceNotFound, DatabaseError)):
        return game_json, {}

    error_code = ServerOk(method='GET')
    return  error_code, game_json


def update_boggle_game(game_id, token, word, **kwargs):
    game_json = game_model_manager.update_game(game_id, token, word, full=True)
    if isinstance(game_json, (ResourceNotFound, DatabaseError, OperationNotSupported)):
        return game_json, {}

    error_code = ServerOk(method='PUT')
    return error_code, game_json


def create_boggle_game(duration, random, board_string=None, **kwargs):
    token = token_manager.generate_random_token()

    corpus_json = corpus_model_manager.get_or_create_corpus(
        DEFAULT_CORPUS_NAME, DEFAULT_CORPUS_PATH
    )

    board_json = board_model_manager.get_or_create_boggle_board(
        random=random, board_string=board_string,
        corpus_id=corpus_json['id'])
    
    if isinstance(board_json, (OperationNotSupported, DatabaseError)):
        return board_json, {}

    game_json = game_model_manager.create_game(
        duration=duration, token=token,
        board_id=board_json['id'])

    if isinstance(game_json, (OperationNotSupported, DatabaseError)):
        return game_json, {}

    error_code = ServerOk(method='POST')
    return error_code, game_json
