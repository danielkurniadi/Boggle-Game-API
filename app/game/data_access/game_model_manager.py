from app import db
from app.game.models.game_model import Game
from app.bridge.decorators.db_exception import (
    db_exception
)
from app.bridge.error.error_code import (
    OperationNotSupported
)

TOKEN_LENGTH = 32


# ---------------------
# GAME
# ---------------------

@db_exception
def get_game_by_id(game_id):
    return Game.objects(id=game_id).first()


@db_exception
def get_game_by_token(token):
    return Game.objects(token=token).first()


@db_exception
def create_game(duration, token, board_id):
    game = Game(token=token, duration=duration, board=board_id)
    game.save()

    return game


@db_exception
def update_game(game_id, token, word):
    word = word.upper()
    game = Game.objects(id=game_id, token=token).first()

    if game is None:
        return game

    board = game.board

    if game.check_expired():
        return OperationNotSupported("Outdated Game. Time's Up.")

    if not board.check_answer(word):
        return OperationNotSupported("Wrong answer: %s" % word)
    
    if not game.check_repeat(word):
        # add points for correct answer
        # which is not a repeat
        game.found_words.append(word)
        game.increment_points()
        game.save()

    return game


@db_exception
def delete_game_by_id(game_id):
    game = Game.objects(id=game_id).first()
    if game is not None:
        game.delete()
    return game
