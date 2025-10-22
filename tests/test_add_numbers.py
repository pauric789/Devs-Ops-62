import sys
import types
import pytest


# --- Workaround to import add_numbers without running input() code ---
# We'll manually import the function definition only, skipping execution.

addNumbers = types.ModuleType("addNumbers")

with open("addNumbers.py") as f:
    code_lines = f.readlines()

# Extract only the function definition (before the input prompts)
func_code = ""
for line in code_lines:
    if line.strip().startswith("num1"):
        break
    func_code += line

exec(func_code, addNumbers.__dict__)

# Now we can test safely
add_numbers = addNumbers.add_numbers


# --- TESTS ---
def test_add_two_positive_numbers():
    assert add_numbers(2, 3) == 5


def test_add_negative_and_positive():
    assert add_numbers(-1, 4) == 3


def test_add_two_negatives():
    assert add_numbers(-2, -3) == -5


def test_add_zero_and_number():
    assert add_numbers(0, 7) == 7
    assert add_numbers(7, 0) == 7


def test_add_floats():
    assert add_numbers(2.5, 3.5) == pytest.approx(6.0)

