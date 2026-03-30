from quadratic_equation import solve_quadratic_equation as solve

def test_quadratic_equation():
    assert solve(1, -3, 2) == (1, 2)

def test_float_values():
    assert solve(1, -4, 3.75) == (1.5, 2.5)

def test_one_solution():
    assert solve(1, -4, 4) == (2,)

def test_zero_solution():
    assert solve(10, 2, 1) == tuple()