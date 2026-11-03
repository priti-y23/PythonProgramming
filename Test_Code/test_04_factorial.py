import os
import importlib.util

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

MODULE_PATH = os.path.join(
    BASE_DIR, "Code", "04_factorial.py"
)

spec = importlib.util.spec_from_file_location(
    "factorial_module", MODULE_PATH
)

m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_positive():
    assert m.factorial(5) == 120


def test_zero():
    assert m.factorial(0) == 1


def test_one():
    assert m.factorial(1) == 1


def test_negative():
    try:
        m.factorial(-5)
        assert False
    except ValueError:
        assert True