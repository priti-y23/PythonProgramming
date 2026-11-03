import sys
sys.path.append("Code")

from reverse_number import reverse_number


def test_reverse_number():
    assert reverse_number(12345) == 54321
    assert reverse_number(123) == 321
    assert reverse_number(100) == 1
    assert reverse_number(7) == 7
    assert reverse_number(-123) == -321


if __name__ == "__main__":
    test_reverse_number()
    print("All tests passed!")