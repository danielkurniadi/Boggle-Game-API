from tests.data import (
    create_boggle_matrix, create_solution,
    create_corpus_words, create_wrong_words,
    rand_string
)

import pytest
from app import flask_app


@pytest.fixture
def client():
    from app import flask_app
    yield flask_app


# ------------------
# BOGGLE BOARD
# ------------------

@pytest.fixture
def boggle_matrix():
    return create_boggle_matrix()


@pytest.fixture
def board_string():
    return 'ACEDLUG*E*HTGAFK'


@pytest.fixture
def solution():
    return create_solution()


@pytest.fixture
def corpus_words():
    return create_corpus_words()


@pytest.fixture
def wrong_words():
    return create_wrong_words()
