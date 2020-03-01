import os
import string
import random

from app.game.models.game_model import Game
from app.game.models.board_model import Board
from app.game.models.corpus_model import Corpus

from tests import TEST_DIR


__all__ = [
    'rand_string', 'create_solution', 'create_corpus_words',
    'create_wrong_words'
]


def rand_string(minlength=0, maxlength=10):
    length = random.randint(minlength, maxlength)
    return ''.join(random.choices(string.ascii_uppercase, k=length))


def create_solution():
    solution_file = os.path.join(TEST_DIR, 'data/test_solution.txt')
    solution = []
    with open(solution_file, 'r') as fp:
        for line in fp:
            solution.append(line.strip())
    return solution


def create_corpus_words():
    corpus_file = os.path.join(TEST_DIR, 'data/test_dictionary.txt')
    corpus = []
    with open(corpus_file, 'r') as fp:
        for line in fp:
            corpus.append(line.strip())
    return corpus


def create_wrong_words():
    wrong_words_file = os.path.join(TEST_DIR, 'data/test_wrong.txt')
    wrong_words = []
    with open(wrong_words_file, 'r') as fp:
        for line in fp:
            wrong_words.append(line.strip())
    return wrong_words
