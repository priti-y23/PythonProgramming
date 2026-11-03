import importlib

module = importlib.import_module("Code.15_second_largest")

second_largest = module.second_largest


def test_second_largest():
    assert second_largest([10, 20, 30, 40, 50]) == 40
    assert second_largest([5, 1, 8, 3, 6]) == 6
    assert second_largest([10, 10, 5, 8]) == 8
    assert second_largest([1, 2]) == 1
    assert second_largest([5]) is None