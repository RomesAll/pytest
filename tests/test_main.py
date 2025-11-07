from src.main import Calculator
import pytest

@pytest.mark.parametrize("x, y, res", 
                         [(1, 2, 0.5), (4, 2, 2), (5, -1, -5)])
def test_divide(x, y, res):
    assert Calculator().divide(x, y) == res

@pytest.mark.parametrize("x, y, res", 
                         [(1, 2, 3), (4, 2, 6), (5, -1, 4)])
def test_sum(x, y, res):
    assert Calculator().add(x, y) == res
