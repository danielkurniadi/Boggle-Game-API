from app.game.data_access.corpus_model_manager import build_prefix_trie
from app.game.data_access.boogle_model_manager import (
    solve_boggle_board,
    boggle_string_to_matrix
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


def test_convert_string_to_matrix(boggle_string):
    boggle_matrix = boggle_string_to_matrix(boggle_string)
    N = len(boggle_matrix)
    M = len(boggle_matrix)

    assert N * M == len(boggle_string)

    for i in range(N):
        for j in range(M):
            k = i * N + j
            assert boggle_string[k] == boggle_matrix[i][j]
