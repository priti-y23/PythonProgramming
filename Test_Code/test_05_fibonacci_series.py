import os
import importlib.util

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

MODULE_PATH = os.path.join(
    BASE_DIR, "Code", "05_fibonacci_series.py"
)

spec = importlib.util.spec_from_file_location(
    "fibonacci_module", MODULE_PATH
)

m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_fibonacci():
    assert m.fibonacci_series(7) == [0, 1, 1, 2, 3, 5, 8]


def test_zero():
    assert m.fibonacci_series(0) == []


def test_one():
    assert m.fibonacci_series(1) == [0]


def test_negative():
    try:
        m.fibonacci_series(-2)
        assert False
    except ValueError:
        assert True