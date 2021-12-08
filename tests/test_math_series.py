import pytest
from math_series.math_series import fibonacci
from math_series.math_series import lucas
from math_series.math_series import sum_series

from math_series import __version__

def test_version():
    assert __version__ == '0.1.0'

def fib_eq(n):
    a = (1 + 5 ** 0.5) / 2
    b = (1 - 5 ** 0.5) / 2
    return round((a ** n - b ** n) / 5 ** 0.5)

def lucas_eq(n):
    return fib_eq(n-1) + fib_eq(n+1)

def test_fib_for_nth():
    assert fibonacci(3) == fib_eq(3)
    assert fibonacci(5) == fib_eq(5)
    assert fibonacci(8) == fib_eq(8)

def test_lucas_for_nth():
    assert lucas(7) == lucas_eq(7)
    assert lucas(11) == lucas_eq(11)
    assert lucas(18) == lucas_eq(18)

def test_sum_series_for_nth():
    assert sum_series(3) == fib_eq(3)
    assert sum_series(5) == fib_eq(5)
    assert sum_series(7, 2, 1) == lucas_eq(7)
    assert sum_series(11, 2, 1) == lucas_eq(11)

