import os


def load_words_from_corpus_file(corpus_file):
    """ Load list of words from corpus file
    :type corpus_file: str
    :rtype List[str]
    """
    if not os.path.isfile(corpus_file):
        raise FileNotFoundError(
            'Corpus File containing words not found in path: %s' % corpus_file)

    words = []
    with open(corpus_file, 'r') as fp:
        for line in fp:
            words.append(line.strip())

    return words
