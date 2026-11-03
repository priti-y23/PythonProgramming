import os
import importlib.util

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

MODULE_PATH = os.path.join(
    BASE_DIR, "Code", "03_pos_neg_zero.py"
)

spec = importlib.util.spec_from_file_location(
    "pos_neg_zero", MODULE_PATH
)

m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_positive():
    assert m.check_number(5) == "Positive"


def test_negative():
    assert m.check_number(-5) == "Negative"


def test_zero():
    assert m.check_number(0) == "Zero"
    