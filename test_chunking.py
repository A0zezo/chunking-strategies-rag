import pytest
from chunking import *


def test_fixed_overlap_content():
    c = fixed_chunks("abcdefghij", size=4, overlap=2)
    assert c[0] == "abcd" and c[1] == "cdef"


def test_fixed_covers_text():
    t = "x" * 95
    assert "".join(fixed_chunks(t, 20, 0)) == t


def test_bad_overlap():
    with pytest.raises(ValueError):
        fixed_chunks("abc", 5, 5)


def test_sentence_never_splits_sentence():
    c = sentence_chunks("One two. Three four. Five six.", 12)
    assert c == ["One two.", "Three four.", "Five six."]


def test_paragraphs():
    assert paragraph_chunks("a\n\nb\n\n\nc") == ["a", "b", "c"]
