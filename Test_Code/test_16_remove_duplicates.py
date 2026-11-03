import importlib

module = importlib.import_module("Code.16_remove_duplicates")

remove_duplicates = module.remove_duplicates


def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 4, 4]) == [1, 2, 3, 4]
    assert remove_duplicates([1, 1, 1, 2, 2, 3]) == [1, 2, 3]
    assert remove_duplicates([5, 4, 5, 3, 4]) == [5, 4, 3]
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
    assert remove_duplicates([]) == []