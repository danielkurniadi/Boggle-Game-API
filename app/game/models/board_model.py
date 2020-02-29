import mongoengine
from datetime import datetime, timedelta

from app import flask_app, db
from app.game.models.corpus_model import Corpus

BOARD_REGEXP = r"^[a-zA-Z\*]+$"


class Board(db.Document):
    """ Board Model Definition
    """

    board_string    = db.StringField(required=True, regex=BOARD_REGEXP,
                            max_length=16, min_length=16)
    solution        = db.ListField(db.StringField(max_length=16))
    corpus          = db.ReferenceField(Corpus, reverse_delete_rule=mongoengine.DO_NOTHING)

    def to_json(self, full=False):
        board_json = {
            'id': str(self.id),
            'board_string': self.board_string,
        }
        return board_json

    def check_answer(self, word):
        return (word in self.solution)

    def __repr__(self):
        return "<Board: id = %s>" % self.id
