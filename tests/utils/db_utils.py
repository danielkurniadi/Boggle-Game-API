import os
import json

from collections import OrderedDict
from functools import wraps

from tests import TEST_DIR
from app import db


def strip_non_valid_character(lines):
    return [line.strip('\n').strip(' ') for line in lines]


def save_to_db(model_dicts, field_to_models):
    for field, model_obj in field_to_models.items():
        for model_dict in model_dicts[field]:
            model_obj(**model_dict).save()
            print('model {} is created'.format(field))


def setup_all_models():
    from app.game.models.corpus_model import Corpus
    from app.game.models.board_model import Board
    from app.game.models.game_model import Game

    field_to_models = OrderedDict()

    # mapping field as model name to ORM Class
    field_to_models['corpus'] = Corpus
    field_to_models['boards'] = Board
    field_to_models['games'] = Game

    model_dicts = {}

    corpus_schema_file = os.path.join(TEST_DIR, 'schema/', 'corpus.json')
    with open(corpus_schema_file, 'r') as fp:
        corpus_schema = json.loads(''.join(strip_non_valid_character(fp.readlines())))
        model_dicts.update(corpus_schema)

    board_schema_file = os.path.join(TEST_DIR, 'schema/', 'board.json')
    with open(board_schema_file, 'r') as fp:
        board_schema = json.loads(''.join(strip_non_valid_character(fp.readlines())))
        model_dicts.update(board_schema)

    game_schema_file = os.path.join(TEST_DIR, 'schema/', 'game.json')
    with open(game_schema_file, 'r') as fp:
        game_schema = json.loads(''.join(strip_non_valid_character(fp.readlines())))
        model_dicts.update(game_schema)
    
    save_to_db(model_dicts, field_to_models)
