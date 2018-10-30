from mysoftware import *
import pytest

def test_square_integers():
    assert square(2) == 4
    assert square(0) == 0
    assert square(-1) == 1
    assert square(3) == 9

def test_coulomb():
    assert coulomb(2.0) == 0.5
    assert coulomb(4.0) == 0.25
    assert coulomb(-1.0) == -1.0
    assert coulomb(3.0) == 1.0/3.0
    with pytest.raises(ZeroDivisionError):
         coulomb(0.0)
