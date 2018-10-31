import numpy as np

def square(x):
    """
    Takes a number x and squares it.

    Parameters:
    -----------
    x, float or int:
        Number which is to be squared.

    Returns:
    --------
    float:
        Square of x

    Examples:
    ---------
    >>> square(2)
    4

    >>> square(-1)
    1

    """
    return x*x

def coulomb(r):
    return 1.0/r

def CentralDifference(f, x, h):
   # f(x + h) - f(x - h)
   # ------------------    \approx f'(x)
   #         2*h
   return (f(x + h) - f(x - h))/(2*h)

def myfunc(x):
    return (x**2 + (x - 2)**3 - 5)

def mysinfunc(x):
    return (np.sin(x**2) - x + 5)

def mysquaredfunc(x):
    return (x - 2)**2

def mytanfunc(x):
    return np.tan(x)

def mybisection(func, a, b, eps):
    fa = func(a)
    fb = func(b)
    if fa * fb > 0:
        print('No root between these bounds')
        return None
    while abs(b - a) > eps:
        x = 0.5 * (a + b)
        fx = func(x)
        if fa * fx < 0:
            b = x
        else:
            a = x
    return x
