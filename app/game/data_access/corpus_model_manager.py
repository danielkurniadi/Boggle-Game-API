import os

from app import flask_app
from app.bridge.error.error_code import OperationNotSupported
from app.bridge.managers.file_manager import load_words_from_corpus_file
from app.game.models.corpus_model import Corpus, PrefixTrieNode


CORPUS_PATH = flask_app.config['CORPUS_PATH']


# --------------------------
# PREFIX TRIE
# --------------------------

def get_or_create_corpus(corpus_path=CORPUS_PATH):
    corpus = Corpus.objects(filepath=corpus_path).first()

    if corpus is None:
        if not os.path.isfile(corpus_path):
            # Path must be given relative to config.BASEDIR 
            raise OperationNotSupported(
                "Neither the Corpus is saved in DB "
                "nor it is found in specified path: %s" % corpus_path
            )
        corpus_words = load_words_from_corpus_file(corpus_path)
        prefix_trie = build_prefix_trie(words)

        corpus = Corpus(filepath = corpus_path, name=corpus_path.split('.')[0])
        corpus.save()

    return corpus.to_json()


def build_prefix_trie(words):
    prefix_trie = PrefixTrieNode()
    for word in words:
        prefix_trie.insert(word)

    return prefix_trie
