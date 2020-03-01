import bson
from app import db
from app.game.data_access import board_model_manager
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
        return ResourceNotFound("Outdated Game. Time's Up.")

    return game


@db_exception
def get_game_by_token(token):
    if not bson.ObjectId.is_valid(game_id):
        return ResourceNotFound('Invalid game_id.')

    game = Game.objects(token=token).first()

    if isinstance(game, Game) and game.check_expired():
        game.delete()
        return ResourceNotFound("Outdated Game. Time's Up.")

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

    word = word.upper()
    game = Game.objects(id=game_id, token=token).first()

    if not isinstance(game, Game):
        return game

    if game.check_expired():
        return ResourceNotFound("Outdated Game. Time's Up.")

    board_string = game.board.board_string
    prefix_trie = game.board.corpus.prefix_trie
    if not board_model_manager.validate_board_answer(
        word, board_string, prefix_trie):
        return OperationNotSupported("Wrong answer: %s" % word.lower())

    if game.check_repeat(word) == False:
        game.found_words.append(word)
        game.increment_points(len(word))
        game.save()

    return game


@db_exception
def delete_game_by_id(game_id):
    game = Game.objects(id=game_id).first()
    if game is not None:
        game.delete()
    return game
