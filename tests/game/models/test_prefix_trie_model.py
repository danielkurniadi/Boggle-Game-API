from app.game.models.corpus_model import PrefixTrieNode


# --------------------
# PREFIX TRIE
# --------------------

def test_prefix_trie_create():
    trie = PrefixTrieNode()
    assert len(trie) == 0


def test_prefix_trie_insert(corpus_words):
    trie = PrefixTrieNode()

    for word in corpus_words:
        trie.insert(word)

    assert len(trie) != 0


def test_prefix_trie_contain(corpus_words):
    trie = PrefixTrieNode()

    for word in corpus_words:
        trie.insert(word)
        assert trie.check_contain(word) == True


def test_prefix_trie_not_contain(corpus_words, wrong_words):
    trie = PrefixTrieNode()

    for word in corpus_words:
        trie.insert(word)

    for wrong_word in wrong_words:
        assert trie.check_contain(wrong_word) == False


def test_prefix_autoset_key():
    trie = PrefixTrieNode()
    child_trie = trie['A']
    subchild_trie = child_trie['Z']

    assert isinstance(child_trie, PrefixTrieNode)
    assert isinstance(subchild_trie, PrefixTrieNode)

    assert len(trie) == 1
    assert len(child_trie) == 1
    assert len(subchild_trie) == 0
