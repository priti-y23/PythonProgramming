import importlib

module = importlib.import_module("Code.11_vowels_consonants")

count_vowels_consonants = module.count_vowels_consonants


def test_count_vowels_consonants():
    assert count_vowels_consonants("hello") == (2, 3)
    assert count_vowels_consonants("Python") == (1, 5)
    assert count_vowels_consonants("AEIOU") == (5, 0)
    assert count_vowels_consonants("12345") == (0, 0)
    assert count_vowels_consonants("Hello World") == (3, 7)