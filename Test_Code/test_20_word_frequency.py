import importlib

module = importlib.import_module("Code.20_word_frequency")

word_frequency = module.word_frequency


def test_word_frequency():
    assert word_frequency("hello world hello") == {
        "hello": 2,
        "world": 1
    }

    assert word_frequency("Python is easy Python") == {
        "python": 2,
        "is": 1,
        "easy": 1
    }

    assert word_frequency("one two three") == {
        "one": 1,
        "two": 1,
        "three": 1
    }

    assert word_frequency("") == {}

    assert word_frequency("apple apple banana banana banana") == {
        "apple": 2,
        "banana": 3
    }