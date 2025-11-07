from src.main import Calculator
from contextlib import nullcontext as does_not_raise
import pytest

class TestCalc:
    @pytest.mark.parametrize("x, y, res, expectation", 
                            [(1, 2, 0.5, does_not_raise()), 
                             (4, 2, 2, does_not_raise()), 
                             (5, "-1", -5, pytest.raises(TypeError))])
    def test_divide(self, x, y, res, expectation):
        with expectation:
            assert Calculator().divide(x, y) == res

    @pytest.mark.parametrize("x, y, res", 
                            [(1, 2, 3), (4, 2, 6), (5, -1, 4)])
    def test_sum(self, x, y, res):
        assert Calculator().add(x, y) == res
