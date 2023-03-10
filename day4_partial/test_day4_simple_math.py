#test simple_math.py
import simple_math


def test_simple_add():
    assert simple_math.simple_add(1,2) == 3
    
def test_simple_sub():
    assert simple_math.simple_sub(5,2) == 3

def test_simple_mult():
    assert simple_math.simple_mult(5,2) == 10

def test_simple_div():
    assert simple_math.simple_div(5,2) == 2.5

def test_poly_first():
    assert simple_math.poly_first(2,5,8) == 21

def test_poly_second():
    assert simple_math.poly_second(2,5,8,3) == 33