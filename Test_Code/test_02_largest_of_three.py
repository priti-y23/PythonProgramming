import importlib

m = importlib.import_module("Code.02_largest_of_three")

assert m.largest_of_three(10, 25, 15) == 25
assert m.largest_of_three(5, 2, 1) == 5
assert m.largest_of_three(-1, -5, -2) == -1

print("Test 2 passed")