import string
import random


def rand_string(minlength=0, maxlength=10):
    length = random.randint(minlength, maxlength)
    return ''.join(random.choices(string.ascii_uppercase, k=length))


def create_boggle_matrix():
    return [
        ['A', 'C', 'E', 'D'],
        ['L', 'U', 'G', '*'],
        ['E', '*', 'H', 'T'],
        ['G', 'A', 'F', 'K']
    ]


def create_solution():
    return ['ACE', 'ACED', 'AGE', 'APE', 'CUDA', 'CUE',
            'DIG', 'DO', 'DOG', 'DOGE', 'DOT', 'EEG', 'EIGEN',
            'EIGHT', 'FAR', 'FILE', 'GAS', 'GAUGE', 'GIGA',
            'GUN', 'GUM', 'HEEL', 'HIDE', 'HIT', 'HOLE', 'HUE',
            'HUGE', 'LACE', 'LAUGH', 'LEAF', 'LEG', 'MEGA',
            'THUG', 'TIDE']


def create_corpus_words():
    return ['APACHE', 'BOLD', 'BORN', 'CAST', 'CASTLE',
            'DAY', 'DO', 'DONT', 'DREAM', 'FINE', 'GOOD',
            'GONE', 'KAFKA', 'KISS', 'LEG', 'LIFE', 'LOVE',
            'ROOT', 'TAP', 'TIGER', 'TIME'] \
            + create_solution()


def create_wrong_words():
    invalid = list(string.whitespace) + [' ', '\n', '*', '']
    not_there = ['TAP', 'TIME', 'ROOT', 'GONE', 'DREAM']
    incomplete = ['AC', 'AG', 'LAU', 'LAC', 'HU', 'HUG', 'LE', 'TID']
    extended = [word + 'Z' for word in create_solution()]

    return invalid + incomplete + extended
