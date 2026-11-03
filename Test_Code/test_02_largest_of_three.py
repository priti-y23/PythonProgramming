import importlib.util
from pathlib import Path

code_path = (
    Path(__file__).resolve().parents[1]
    / "Code"
    / "02_largest_of_three.py"
)

spec = importlib.util.spec_from_file_location(
    "largest", code_path
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

assert mod.largest_of_three(3, 9, 4) == 9
assert mod.largest_of_three(-5, -2, -8) == -2
assert mod.largest_of_three(4, 4, 1) == 4

print("Test 02 passed")