import importlib

module = importlib.import_module("Code.17_common_elements")

common_elements = module.common_elements


def test_common_elements():
    assert common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
    assert common_elements([1, 2, 3], [4, 5, 6]) == []
    assert common_elements([1, 2, 2, 3], [2, 3, 4]) == [2, 3]
    assert common_elements(["apple", "banana"], ["banana", "orange"]) == ["banana"]
    assert common_elements([], [1, 2, 3]) == []