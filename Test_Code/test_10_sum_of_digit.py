import sys
sys.path.append("Code")

from importlib import import_module

sum_digits = import_module("10_sum_of_digits")

assert sum_digits.sum_of_digits(123) == 6
assert sum_digits.sum_of_digits(456) == 15
assert sum_digits.sum_of_digits(100) == 1
assert sum_digits.sum_of_digits(9) == 9

print("All test cases passed!")