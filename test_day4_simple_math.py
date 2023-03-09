#test simple_math.py
import day4_simple_math


def test_simple_add():
    assert day4_simple_math.simple_add(1,2) == 3
    
def test_simple_sub():
    assert day4_simple_math.simple_sub(5,2) == 3

def test_simple_mult():
    assert day4_simple_math.simple_mult(5,2) == 10

def test_simple_div():
    assert day4_simple_math.simple_div(5,2) == 2.5

def test_poly_first():
    assert day4_simple_math.poly_first(2,5,8) == 21

def test_poly_second():
    assert day4_simple_math.poly_second(2,5,8,3) == 33