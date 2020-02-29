import os

from app.bridge.decorators.db_exception import db_exception
from app.bridge.error.error_code import OperationNotSupported
from app.bridge.managers.corpus_file_manager import load_words_from_corpus_file
from app.game.models.corpus_model import Corpus, PrefixTrieNode


# --------------------------
# MODEL MANAGER
# --------------------------

@db_exception
def get_corpus_by_name(name):
    corpus = Corpus.objects(name=name).first()
    return corpus


@db_exception
def get_or_create_corpus(corpus_name, corpus_path):
    corpus = Corpus.objects(name=corpus_name).first()

    if corpus is None:
        if not os.path.isfile(corpus_path):
            # Path must be given relative to config.BASEDIR 
            raise OperationNotSupported(
                "Neither the Corpus is saved in DB "
                "nor it is found in specified path: %s" % corpus_path
            )
        corpus_words = load_words_from_corpus_file(corpus_path)
        prefix_trie = build_prefix_trie(corpus_words)

        corpus = Corpus(filepath=corpus_path, name=corpus_name,
                        prefix_trie=prefix_trie)
        corpus.save()

    return corpus


# --------------------------
# PREFIX TRIE
# --------------------------

def build_prefix_trie(words):
    prefix_trie = PrefixTrieNode()
    for word in words:
        word = word.upper()
        prefix_trie.insert(word)

    return prefix_trie
