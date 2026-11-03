import importlib

module = importlib.import_module("Code.19_find_duplicates")

find_duplicates = module.find_duplicates


def test_find_duplicates():
    assert find_duplicates([1, 2, 3, 2, 4, 1]) == [1, 2]
    assert find_duplicates([1, 1, 2, 2, 3, 3]) == [1, 2, 3]
    assert find_duplicates([1, 2, 3, 4]) == []
    assert find_duplicates([5, 5, 5, 6, 7, 7]) == [5, 7]
    assert find_duplicates([]) == []