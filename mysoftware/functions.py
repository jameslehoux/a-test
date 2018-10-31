
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

def myrugbyfunc(theta, yend, ystart, x, v):
    return ystart - yend + x * np.tan(theta) - (0.5 * (x**2 * 9.81)/(v**2)) * (1 + np.tan(theta)**2)

def myrealrugbyfunc(theta):
    return 1.85 - 1.96 + 20 * np.tan(theta) - (0.5 * (20**2 * 9.81)/(15**2)) * (1 + np.tan(theta)**2)

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

def mytrapz(func,a,b,n):
	integral=0.5*(func(a)+func(b))
	h=(b-a)/n
	x=a
	for i in range(1,n):
		x=x+h
		integral=integral+func(x)
	integral=integral*h
	return integral

def myintegral(x):
	return -(x-2)**2+4

def myfindiff(Ta,Tb,x,tend,T0,alpha,dx,dt):
	nodes = int(x/dx)+1

	Tdist = np.ones(nodes)*T0

	Tdist[0]=Ta
	Tdist[nodes-1]=Tb

	steps = int(tend/dt) + 1
	Tnew = np.zeros(nodes)

	Tnew[0] = Ta
	Tnew[nodes-1] = Tb

	for p in range(1,steps):
		for i in range (1,nodes - 1):
			Tnew[i] = ((alpha * dt) / dx**2) * (Tdist[i+1] + Tdist[i-1])\
			 + (1 - ((2*alpha*dt)/(dx**2)))*Tdist[i]

		print(Tdist)
		Tdist = Tnew[:]
		print(Tdist)

	return Tdist
