import importlib

module = importlib.import_module("Code.18_missing_number")

find_missing_number = module.find_missing_number


def test_find_missing_number():
    assert find_missing_number([1, 2, 3, 5]) == 4
    assert find_missing_number([1, 2, 3, 4, 6]) == 5
    assert find_missing_number([1, 2, 4, 5]) == 3
    assert find_missing_number([2, 3, 4, 5]) == 1
    assert find_missing_number([1]) == 2