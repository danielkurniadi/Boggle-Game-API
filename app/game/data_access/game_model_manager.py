from app import db
from app.game.models.game_model import Game
from app.bridge.managers import (
    token_manager
)
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
    return Game.objects(id=game_id).first().to_json(full=True)


@db_exception
def get_game_by_token(token):
    return Game.objects(token=token).first().to_json(full=True)


@db_exception
def create_game(duration, random, board=""):
    board = boogle_manager.create_boggle_board(random=random, board_string=board)
    token = token_manager.generate_token(length=TOKEN_LENGTH)
    game = Game.objects(token=token, duration=duration)

    board.save()
    game.board = board
    game.save()

    return game.to_json()


@db_exception
def update_game(game_id, token, word):
    game = Game.objects(id=game_id, token=token)
    board = game.board

    if board.check_word(word):
        if not word in game.found_words:
            game.found_words.append(word)
            game.save()
        return game.to_json(full=True)

    raise OperationNotSupported(
        "Wrong Answer to Boggle Board: word=%s, id=%s"
        % (word, board.id)
    )


@db_exception
def delete_game_by_id(game_id):
    Game.objects(id=game_id).delete()
    return True
