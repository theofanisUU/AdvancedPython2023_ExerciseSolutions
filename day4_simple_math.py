"""
A collection of simple math operations
"""

def simple_add(a,b):
    """
    Simple function to add 2 numbers

    Parameters
    ----------
    a : float
        first number to be added.
    b : float
        second number to be added.

    Returns
    -------
    float
        The sum of the 2 parameters "a" and "b".
        
    Examples
    -------
    simple_add(2,5)
    >>>7

    """
    return a+b

#-----------------------------
def simple_sub(a,b):
    """
    Simple function to substract 2 numbers

    Parameters
    ----------
    a : float
        Number to be substructed from.
    b : float
        Number to substract from "a"

    Returns
    -------
    float
        The result of substraction of "b" from "a".
        
    Examples
    -------
    simple_sub(2,5)
    >>>-3
    simple_sub(7,5)
    >>>2

    """
    return a-b

#-----------------------------
def simple_mult(a,b):
    """
    Simple function for multiplication of 2 numbers

    Parameters
    ----------
    a : float
        First Number to be multiplied
    b : float
        Second Number to be multiplied

    Returns
    -------
    float
        The product of multiplication of "a" and "b".
        
    Examples
    -------
    simple_mult(5,5)
    >>>25
    simple_mult(-3,5)
    >>>-15

    """
    return a*b
#-----------------------------
def simple_div(a,b):
    """
    Simple function for division of 2 numbers

    Parameters
    ----------
    a : float
        Devidend
    b : float
        Divisor, needs to be non-zero

    Returns
    -------
    float
        The result of division of "a" by "b".
        
    Examples
    -------
    simple_div(-3,5)
    >>>-0.6
    simple_div(35,13)
    >>>2.6923076923076925
    simple_div(35,0)
    >>>ZeroDivisionError

    """
    return a/b
#-----------------------------
def poly_first(x, a0, a1):
    """
    Function to return value of a first degree polynomial for given input

    Parameters
    ----------
    x : float
        input for the polynomial function.
    a0 : float
        0th degree coefficient.
    a1 : float
        1st degree coefficient.

    Returns
    -------
    float
        Value of the first degree polynomial for input "x".
     
    Examples
    -------
    poly_first(1, 2, 3)
    >>>5
    poly_first(3, 2, 3)
    >>>11
    """
    return a0 + a1*x

#-----------------------------
def poly_second(x, a0, a1, a2):
    """
    Function to return value of a second degree polynomial for given input

    Parameters
    ----------
    x : float
        input for the polynomial function.
    a0 : float
        0th degree coefficient.
    a1 : float
        1st degree coefficient.
    a2 : float
        2nd degree coefficient.

    Returns
    -------
    float
        Value of the second degree polynomial for input "x".
     
    Examples
    -------
    poly_second(2, 3, 2, 4)
    >>>23
    poly_second(3, 10, 5, 3)
    >>>52

    """
    return poly_first(x, a0, a1) + a2*(x**2)

print(poly_second(3, 10, 5, 3))
# Feel free to expand this list with more interesting mathematical operations...
# .....
