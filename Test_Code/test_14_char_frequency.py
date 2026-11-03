import importlib

module = importlib.import_module("Code.14_char_frequency")

char_frequency = module.char_frequency


def test_char_frequency():
    assert char_frequency("hello") == {
        "h": 1,
        "e": 1,
        "l": 2,
        "o": 1
    }

    assert char_frequency("aabbc") == {
        "a": 2,
        "b": 2,
        "c": 1
    }

    assert char_frequency("abc") == {
        "a": 1,
        "b": 1,
        "c": 1
    }

    assert char_frequency("") == {}