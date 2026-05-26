import pytest

from index import add_numbers

def test_add_numbers_with_positive_integers():
    assert add_numbers(5, 10) == 20

def test_add_numbers_with_negative_values():
    assert add_numbers(-3, -7) == -10
    assert add_numbers(5, -2) == 3

def test_add_numbers_with_zero():
    assert add_numbers(0, 0) == 0
    assert add_numbers(0, 5) == 5
    assert add_numbers(-5, 0) == -5

def test_add_numbers_with_floats():
    assert add_numbers(2.5, 1.5) == pytest.approx(4.0)
    assert add_numbers(0.1, 0.2) == pytest.approx(0.3)

def test_add_numbers_with_large_numbers():
    assert add_numbers(10**12, 10**12) == 2 * 10**12

@pytest.mark.parametrize("value_a,value_b", [
    ("a", 1),
    (1, "b"),
    (None, 1),
    ([1, 2], 3),
])
def test_add_numbers_raises_type_error_for_invalid_types(value_a, value_b):
    with pytest.raises(TypeError):
        add_numbers(value_a, value_b)
