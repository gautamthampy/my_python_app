"""Tests for the calculator module."""

import pytest
from my_app.main import add, subtract, multiply, divide


def test_add():
    """Test the add function."""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2


def test_subtract():
    """Test the subtract function."""
    assert subtract(5, 3) == 2
    assert subtract(2, 3) == -1
    assert subtract(-1, -1) == 0


def test_multiply():
    """Test the multiply function."""
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6


def test_divide():
    """Test the divide function."""
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(-6, 2) == -3

    with pytest.raises(ValueError):
        divide(5, 0)