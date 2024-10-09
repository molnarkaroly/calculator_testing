import pytest
from calculating import *

def test_sum():
    assert sum(1, 2) == 3
    assert sum(1, -2) == -1
    assert sum(0, 0) == 0
    
def test_sub():
    assert sub(2, 1) == 1
    assert sub(1, -2) == 3
    assert sub(0, 0) == 0
    
def test_mult():
    assert mult(0, 0) == 0
    assert mult(2, 1) == 2
    assert mult(3, 3) == 9
    
def test_div():
    assert div(8, 1) == 8
    assert div(9, 3) == 3
    assert div(10, 5) == 2
    assert div(0, 0) == "error"