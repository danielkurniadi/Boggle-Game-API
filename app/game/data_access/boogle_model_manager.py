"""
BOGGLE BOARD MANAGER DEFINITION

Handles boggle board game related operations.
"""
import os
from app.game.models.board_model import Board
from app.game.data_access import corpus_model_manager


# ----------------------
# MANAGER
# ----------------------

def create_boggle_board():
    pass


# ----------------------
# HELPERS
# ----------------------

SIZE = 4
NEIGHBOURS = [(dx, dy) 
              for dx in range(-1, 2)
              for dy in range(-1, 2)
              if not (dx == dy == 0)]


def solve_boggle_board(boggle_matrix, trie_root):
    """ Solve all words found in boggle board matrix
    :rtype: List[str]
    """

    N = len(boggle_matrix)
    M = len(boggle_matrix[0])

    stack = []

    for row in range(N):
        for col in range(M):
            stack.append((row, col, trie_root, set()))
    
    def _solve_boggle(stack):
        # Depth-first search traversal
        while stack:
            row, col, trieNode, seen = stack.pop()

            if "$" in trieNode:
                yield trieNode["$"]

            if not (0 <= row < N and 0 <= col < M) or (row, col) in seen:
                continue
            char = boggle_matrix[row][col]
            nextTrieNodes = []

            if char == "*":
                nextTrieNodes.extend(trieNode[key] for key in trieNode if key != "$")
            elif char not in trieNode:
                continue

            nextTrieNodes.append(trieNode[char])

            for dx, dy in NEIGHBOURS:
                for nextTrieNode in nextTrieNodes:
                    stack.append((row + dy, col + dx, nextTrieNode, seen | {(row, col)}))

    return list(set(_solve_boggle(stack)))


def generate_boggle_board():
    pass


def boggle_string_to_matrix(string):
    if len(string) != SIZE * SIZE:
        raise ValueError("Must enter 4*4 grid (16 characters)")
    return [list(string[i:i+SIZE]) for i in range(0, SIZE*SIZE, SIZE)]
