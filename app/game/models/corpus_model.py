from app import flask_app, db


class Corpus(db.Document):
    """ Corpus Model definition for all available words
    """

    name            = db.StringField(required=True, unique=True)
    filepath        = db.StringField(required=True)
    prefix_trie     = db.DictField(required=True)

    def to_json(self, full=False):
        corpus_json = {
            'id': str(self.id),
            'name': self.name,
            'filepath': self.filepath
        }
        return corpus_json

    def __repr__(self):
        return "<Corpus: name = %s>" % self.name


"""
PREFIX TRIE CLASS DEFINITION
"""

VALUE_SYM = "#"  # mark node with value


class PrefixTrieNode(dict):
    """Prefix Trie Node Definition
    """

    def __init__(self, init_dict={}):
        """ Initialise PrefixTrieNode
        """
        super().__init__(init_dict)

    def check_contain(self, word):
        """ Check prefix trie contains given word
        :type word: str
        """
        current = self
        for char in word:
            if char not in current:
                return False
            current = current[char]
        return current[VALUE_SYM] == word

    def insert(self, word):
        """ Build trie from word
        :type word: str
        """
        assert isinstance(word, str)

        current = self
        for char in word:
            current = current[char]
        current[VALUE_SYM] = word

    def __missing__(self, key):
        """ Handle key is not in PrefixTrieNode
        :type key: str
        """
        self[key] = PrefixTrieNode()
        return self[key]
