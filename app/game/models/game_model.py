import mongoengine
from datetime import datetime, timedelta

from app import flask_app, db
from app.game.models.board_model import Board


POINT_PER_WORD = 10


class Game(db.Document):
    """ Game Model Definition
    """

    token           = db.StringField(required=True, unique=True,
                                    max_length=32, min_length=32)
    duration        = db.IntField(required=True, min_value=0)
    board           = db.ReferenceField(Board, reverse_delete_rule=mongoengine.NULLIFY)

    created         = db.DateTimeField(required=True, default=datetime.utcnow)
    found_words     = db.ListField(db.StringField(max_length=16))
    points          = db.IntField(default=0, min_value=0)

    @property
    def timeleft(self):
        elapsed = datetime.utcnow() - self.created
        return self.duration - int(elapsed.total_seconds())

    def check_expired(self):
        return self.timeleft < 0

    def check_repeat(self, word):
        return (word in self.found_words)

    def increment_points(self, point):
        self.points += point

    def to_json(self, full=False):
        board = ', '.join(self.board.board_string)
        game_json = {
            'id'    : str(self.id),
            'token' : self.token,
            'board' : board,
            'duration': self.duration
        }

        if full == True:
            game_json.update({
                'time_left' : self.timeleft,
                'points'    : self.points
            })

        return game_json

    def __repr__(self):
        return "<Game: id = %s>" % self.id
