import os
import importlib.util


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

MODULE_PATH = os.path.join(
    BASE_DIR, "Code", "06_primes_number.py"
)


spec = importlib.util.spec_from_file_location(
    "prime_module", MODULE_PATH
)

m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_prime():
    assert m.is_primes(7) == True


def test_not_prime():
    assert m.is_primes(8) == False


def test_zero():
    assert m.is_primes(0) == False


def test_one():
    assert m.is_primes(1) == False


def test_two():
    assert m.is_primes(2) == True