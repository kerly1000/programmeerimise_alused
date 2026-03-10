import pytest
from quadratic_equation import solve_quadratic_equation as solve

def test_quadratic_equation():
    assert solve(1, -3, 2) == (1, 2)