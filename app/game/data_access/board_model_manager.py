"""
BOGGLE BOARD MANAGER DEFINITION

Handles boggle board game related operations.
"""
import os
import string
import random

from app.game.models.board_model import Board
from app.game.models.corpus_model import VALUE_SYM
from app.game.data_access import corpus_model_manager

from app.bridge.decorators.db_exception import db_exception
from app.bridge.error.error_code import OperationNotSupported


# ----------------------
# MODEL MANAGER
# ----------------------

@db_exception
def get_or_create_boggle_board(random, corpus_id, board_string=None,
                        word_counter=None):
    if random == True and board_string is None:
        board_string = generate_board_string(word_counter)

    elif random == False and board_string is None:
        board_string = 'TAP*EAKSOBRSS*XD'

    # find board with same board string and corpus
    board = Board.objects(board_string=board_string, corpus=corpus_id).first()
    if board is not None:
        return board

    # otherwise create new board
    board = Board(board_string=board_string, corpus=corpus_id)

    # prepare for solving board
    board_matrix = board_string_to_matrix(board_string)
    corpus = board.corpus
    trie_root = corpus.prefix_trie

    # solve board and save solution
    solution = solve_boggle_board(board_matrix, trie_root)
    board.solution = solution
    board.save()

    return board


@db_exception
def get_boggle_board_by_id(board_id):
    return Board.objects(id=board_id).first()


# ----------------------
# HELPERS
# ----------------------

SIZE = 4
SPECIAL_CHAR = '*'
NEIGHBOURS = [(dx, dy) 
              for dx in range(-1, 2)
              for dy in range(-1, 2)
              if not (dx == dy == 0)]


def solve_boggle_board(board_matrix, trie_root):
    N = len(board_matrix)
    M = len(board_matrix[0])

    stack = []

    for row in range(N):
        for col in range(M):
            stack.append((row, col, trie_root, set()))

    def _solve_boggle(stack):
        # Depth-first search traversal in iterative
        while stack:
            row, col, trieNode, seen = stack.pop()

            if VALUE_SYM in trieNode:
                yield trieNode[VALUE_SYM]

            if not (0 <= row < N and 0 <= col < M) or (row, col) in seen:
                continue
            char = board_matrix[row][col]
            nextTrieNodes = []

            if char == SPECIAL_CHAR:
                nextTrieNodes.extend(
                    trieNode[key] 
                    for key in trieNode if key != VALUE_SYM
                )
            elif not (char in trieNode):
                continue
            else:
                nextTrieNodes.append(trieNode[char])

            for dx, dy in NEIGHBOURS:
                for nextTrieNode in nextTrieNodes:
                    stack.append((row + dy, col + dx, nextTrieNode, seen | {(row, col)}))

    return list(set(_solve_boggle(stack)))


def generate_board_string(word_counter=None):
    if word_counter is None:
        return ''.join(random.choices(string.ascii_uppercase + '*' * 2, k=SIZE*SIZE))

    choices = string.ascii_uppercase + '*'
    word_counter['*'] = 2000
    weights = [word_counter[ch] for ch in choices]

    return ''.join(random.choices(choices, weights=weights, k=SIZE*SIZE))


def board_string_to_matrix(string):
    if len(string) != SIZE * SIZE:
        raise ValueError("Must enter 4*4 grid (16 characters)")

    return [list(string[i:i+SIZE])
            for i in range(0, SIZE*SIZE, SIZE)]
