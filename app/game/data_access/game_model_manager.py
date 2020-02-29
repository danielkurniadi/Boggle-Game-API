import bson
from app import db
from app.game.models.game_model import Game
from app.bridge.decorators.db_exception import (
    db_exception
)
from app.bridge.error.error_code import (
    OperationNotSupported, ResourceNotFound
)

TOKEN_LENGTH = 32


# ---------------------
# GAME
# ---------------------

@db_exception
def get_game_by_id(game_id):
    if not bson.ObjectId.is_valid(game_id):
        return ResourceNotFound('Invalid game_id.')

    game = Game.objects(id=game_id).first()

    if isinstance(game, Game) and game.check_expired():
        game.delete()
        return OperationNotSupported("Outdated Game. Time's Up.")

    return game


@db_exception
def get_game_by_token(token):
    if not bson.ObjectId.is_valid(game_id):
        return ResourceNotFound('Invalid game_id.')

    game = Game.objects(token=token).first()

    if isinstance(game, Game) and game.check_expired():
        game.delete()
        return OperationNotSupported("Outdated Game. Time's Up.")

    return game


@db_exception
def create_game(duration, token, board_id):
    game = Game(token=token, duration=duration, board=board_id)
    game.save()

    return game


@db_exception
def update_game(game_id, token, word):
    if not bson.ObjectId.is_valid(game_id):
        return ResourceNotFound('Invalid game_id.')

    upper_word = word.upper()
    game = Game.objects(id=game_id, token=token).first()

    if game is None:
        return game

    board = game.board

    if game.check_expired():
        return OperationNotSupported("Outdated Game. Time's Up.")

    if not board.check_answer(upper_word):
        return OperationNotSupported("Wrong answer: %s" % word)
    
    if not game.check_repeat(upper_word):
        game.found_words.append(upper_word)
        game.increment_points(len(upper_word))
        game.save()

    return game


@db_exception
def delete_game_by_id(game_id):
    game = Game.objects(id=game_id).first()
    if game is not None:
        game.delete()
    return game
