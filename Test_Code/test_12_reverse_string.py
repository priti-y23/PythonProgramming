import importlib

module = importlib.import_module("Code.12_reverse_string")

reverse_string = module.reverse_string


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("abc") == "cba"
    assert reverse_string("12345") == "54321"
    assert reverse_string("") == ""