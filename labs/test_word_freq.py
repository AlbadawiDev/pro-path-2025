import pytest
from labs.word_freq import word_frequencies


def test_unicode_and_punctuation():
    assert word_frequencies('Árbol, árbol; SOL! sol\nsol.') == [('sol', 3), ('árbol', 2)]


def test_empty_text():
    assert word_frequencies('...') == []


def test_limit_and_invalid_limit():
    assert len(word_frequencies('one two three', limit=2)) == 2
    with pytest.raises(ValueError):
        word_frequencies('one', limit=-1)
