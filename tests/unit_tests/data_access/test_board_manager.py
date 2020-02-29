from app.game.data_access.corpus_model_manager import build_prefix_trie
from app.game.data_access.board_model_manager import (
    solve_boggle_board,
    generate_board_string,
    board_string_to_matrix
)

# ----------------------
# BOGGLE MANAGER
# ----------------------

def test_solve_board(corpus_words, boggle_matrix, solution):
    trie_root = build_prefix_trie(corpus_words)
    found_words = solve_boggle_board(boggle_matrix, trie_root)

    solution.sort()
    found_words.sort()

    assert found_words == solution


def test_generate_board_string():
    board_string = generate_board_string()
    assert len(board_string) == 16


def test_convert_string_to_matrix(board_string):
    boggle_matrix = board_string_to_matrix(board_string)
    N = len(boggle_matrix)
    M = len(boggle_matrix)

    assert N * M == len(board_string)

    for i in range(N):
        for j in range(M):
            k = i * N + j
            assert board_string[k] == boggle_matrix[i][j]
