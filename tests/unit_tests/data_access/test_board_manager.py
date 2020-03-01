import pytest
import string

from app.game.data_access.corpus_model_manager import build_prefix_trie
from app.game.data_access import board_model_manager
from app.game.data_access.board_model_manager import (
    solve_boggle_board,
    generate_board_string,
    board_string_to_matrix,
    validate_board_answer
)


# ----------------------
# BOGGLE MANAGER
# ----------------------

def test_generate_board_string():
    # run generate board string
    board_string = generate_board_string()

    # check length of generated string
    assert len(board_string) == 16
    
    # check characeter in board string
    for char in board_string:
        assert (char == '*') or (char in string.ascii_uppercase)

@pytest.mark.dependency()
def test_convert_string_to_matrix(board_string):
    # run convert boggle string to matrix form
    boggle_matrix = board_string_to_matrix(board_string)

    # check size/shape of the matrix
    N = len(boggle_matrix)
    M = len(boggle_matrix)
    assert N * M == len(board_string)

    # check correctness for the characters order
    for i in range(N):
        for j in range(M):
            k = i * N + j
            assert board_string[k] == boggle_matrix[i][j]


@pytest.mark.dependency(depends=[
    "test_convert_string_to_matrix",
    # "tests/unit_tests/models/test_prefix_trie_model.py::test_prefix_trie_contain"
])
def test_solve_boggle_board(corpus_words, board_string, solution):
    trie_root = build_prefix_trie(corpus_words)

    # run boggle solver
    found_words = solve_boggle_board(board_string, trie_root)

    # sorting and assert equals lists
    assert sorted(found_words) == sorted(solution)


@pytest.mark.dependency(depends=["test_convert_string_to_matrix"])
def test_validate_board_answer(corpus_words, board_string, solution, wrong_words):
    trie_root = build_prefix_trie(corpus_words)

    # check that solution word is evaluated to correct
    for word in solution:
        assert validate_board_answer(word, board_string, trie_root) == True

    # check that non solution word is evaluated to incorrect
    for word in wrong_words:
        assert validate_board_answer(word, board_string, trie_root) == False
