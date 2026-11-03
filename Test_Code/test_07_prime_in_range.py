from Code.07_primes_in_range import primes_in_range


def test_primes_in_range():
    assert primes_in_range(1, 10) == [2, 3, 5, 7]
    assert primes_in_range(10, 20) == [11, 13, 17, 19]
    assert primes_in_range(1, 2) == [2]
    assert primes_in_range(8, 10) == []


if __name__ == "__main__":
    test_primes_in_range()
    print("All tests passed!")