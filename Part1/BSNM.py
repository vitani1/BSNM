import numpy as np
import math
import matplotlib as npl
import scipy.special
from numpy import abs,sin,cos,e,linspace,pi
from pylab import plot,show,savefig,xlabel,ylabel
from matplotlib import pyplot as plt
print("The code will now be used to calculate various zeroes of the zeroth-order Bessel function using both the bisection and secant methods.")
M = int(input("Please enter in a number for which to truncate the series expansion of the Bessel function:"))
print("Here are the results of the bisection and secant methods applied to the function J0 on the interval [1,3] using values of epsilon of 10^-6, 10^-7, 10^-8, 10^-9, and 10^-10")
print()
def Bessel(M,x): #Defining Bessel Function
	J0 = 1
	for p in range(1,M):
		J0 = J0+(((-1)**p)/(math.factorial(p))**2)*(x/2)**(2*p)
	return J0
N = 0
a = 1
b = 3
c = (a+b)/2
while abs(Bessel(M,c)) > 10**-6:
	if Bessel(M,a)*Bessel(M,c) < 0:
		b = c
		c = (a+b)/2
		N = N + 1
	else:
		a = c
		c = (b+a)/2
		N = N + 1
	if abs(Bessel(M,c)) <= 10**-6:
		print("The root of the function using the bisection method is",c)
		print("The number of iterations is", N)
		print("The value of delta is",abs(b-a))
a = 1
b = 3
roots = []
roots.append(a)
roots.append(b)
for n in range(0,1000):
	roots.append(roots[n+1]-Bessel(M,roots[n+1])*(roots[n+1]-
	roots[n])/(Bessel(M,roots[n+1])-Bessel(M,roots[n])))
	if abs(Bessel(M,roots[n+2])) <= 10**-6:
		print("The root using the secant method is",roots[n+2])
		print("The value of delta is",abs(roots[n+2]-roots[n+1]))
		print("The number of iterations is",n)
		break
N = 0
while abs(Bessel(M,c)) > 10**-7:
	if Bessel(M,a)*Bessel(M,c) < 0:
		b = c
		c = (a+b)/2
		N = N + 1
	else:
		a = c
		c = (b+a)/2
		N = N + 1
	if abs(Bessel(M,c)) <= 10**-7:
		print("The root of the function using the bisection method is",c)
	print("The number of iterations is", N)
	print("The value of delta is",abs(b-a))
a = 1
b = 3
roots = []
roots.append(a)
roots.append(b)
for n in range(0,1000):
	roots.append(roots[n+1]-Bessel(M,roots[n+1])*(roots[n+1]-roots[n])/(Bessel(M,roots[n+1])-Bessel(M,roots[n])))
	if abs(Bessel(M,roots[n+2])) <= 10**-7:
		print("The root using the secant method is",roots[n+2])
		print("The value of delta is",abs(roots[n+2]-roots[n+1]))
		print("The number of iterations is",n)
		break
N = 0
while abs(Bessel(M,c)) > 10**-8:
	if Bessel(M,a)*Bessel(M,c) < 0:
		b = c
		c = (a+b)/2
		N = N + 1
	else:
		a = c
		c = (b+a)/2
		N = N + 1
	if abs(Bessel(M,c)) <= 10**-8:
		print("The root of the function using the bisection method is",c)
		print("The number of iterations is", N)
		print("The value of delta is",abs(b-a))
a = 1
b = 3
roots = []
roots.append(a)
roots.append(b)
for n in range(0,1000):
	roots.append(roots[n+1]-Bessel(M,roots[n+1])*(roots[n+1]-roots[n])/(Bessel(M,roots[n+1])-Bessel(M,roots[n])))
	if abs(Bessel(M,roots[n+2])) <= 10**-8:
		print("The root using the secant method is",roots[n+2])
		print("The value of delta is",abs(roots[n+2]-roots[n+1]))
		print("The number of iterations is",n)
		break
N = 0
while abs(Bessel(M,c)) > 10**-9:
	if Bessel(M,a)*Bessel(M,c) < 0:
		b = c
		c = (a+b)/2
		N = N + 1
	else:
		a = c
		c = (b+a)/2
		N = N + 1
	if abs(Bessel(M,a)) <= 10**-9:
		print("The root of the function using the bisection method is",c)
		print("The number of iterations is", N)
		print("The value of delta is",abs(b-a))
a = 1
b = 3
roots = []
roots.append(a)
roots.append(b)
for n in range(0,1000):
	roots.append(roots[n+1]-Bessel(M,roots[n+1])*(roots[n+1]-roots[n])/(Bessel(M,roots[n+1])-Bessel(M,roots[n])))
	if abs(Bessel(M,roots[n+2])) <= 10**-9:
		print("The root using the secant method is",roots[n+2])
		print("The value of delta is",abs(roots[n+2]-roots[n+1]))
		print("The number of iterations is",n)
		break
N = 0
while abs(Bessel(M,c)) > 10**-10:
	if Bessel(M,a)*Bessel(M,c) < 0:
		b = c
		c = (a+b)/2
		N = N + 1
	else:
		a = c
		c = (b+a)/2
		N = N + 1
	if abs(Bessel(M,c)) <= 10**-10:
		print("The root of the function using the bisection method is",c)
		print("The number of iterations is", N)
		print("The value of delta is",abs(b-a))
a = 1
b = 3
roots = []
roots.append(a)
roots.append(b)
for n in range(0,1000):
	roots.append(roots[n+1]-Bessel(M,roots[n+1])*(roots[n+1]-roots[n])/(Bessel(M,roots[n+1])-Bessel(M,roots[n])))
	if abs(Bessel(M,roots[n+2])) <= 10**-10:
		print("The root using the secant method is",roots[n+2])
		print("The value of delta is",abs(roots[n+2]-roots[n+1]))
		print("The number of iterations is",n)
		break
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
print("Here is the same method on the interval [4,6].")
print()
a = 4
b = 6
c = (a+b)/2
N = 0
while abs(Bessel(M,c)) > 10**-6:
	if Bessel(M,a)*Bessel(M,c) < 0:
		b = c
		c = (a+b)/2
		N = N + 1
	else:
		a = c
		c = (b+a)/2
		N = N + 1
	if abs(Bessel(M,c)) <= 10**-6:
		print("The root of the function using the bisection method is",c)
		print("The number of iterations is", N)
		print("The value of delta is",abs(b-a))
a = 4
b = 6
roots = []
roots.append(a)
roots.append(b)
for n in range(0,1000):
	roots.append(roots[n+1]-Bessel(M,roots[n+1])*(roots[n+1]-roots[n])/(Bessel(M,roots[n+1])-Bessel(M,roots[n])))
	if abs(Bessel(M,roots[n+2])) <= 10**-6:
		print("The root using the secant method is",roots[n+2])
		print("The value of delta is",abs(roots[n+2]-roots[n+1]))
		print("The number of iterations is",n)
		break
N = 0
while abs(Bessel(M,c)) > 10**-7:
	if Bessel(M,a)*Bessel(M,c) < 0:
		b = c
		c = (a+b)/2
		N = N + 1
	else:
		a = c
		c = (b+a)/2
		N = N + 1
	if abs(Bessel(M,c)) <= 10**-7:
		print("The root of the function using the bisection method is",c)
		print("The number of iterations is", N)
		print("The value of delta is",abs(b-a))
a = 4
b = 6
roots = []
roots.append(a)
roots.append(b)
for n in range(0,1000):
	roots.append(roots[n+1]-Bessel(M,roots[n+1])*(roots[n+1]-roots[n])/(Bessel(M,roots[n+1])-Bessel(M,roots[n])))
	if abs(Bessel(M,roots[n+2])) <= 10**-7:
		print("The root using the secant method is",roots[n+2])
		print("The value of delta is",abs(roots[n+2]-roots[n+1]))
		print("The number of iterations is",n)
		break
N = 0
while abs(Bessel(M,c)) > 10**-8:
	if Bessel(M,a)*Bessel(M,c) < 0:
		b = c
		c = (a+b)/2
		N = N + 1
	else:
		a = c
		c = (b+a)/2
		N = N + 1
	if abs(Bessel(M,c)) <= 10**-8:
		print("The root of the function using the bisection method is",c)
		print("The number of iterations is", N)
		print("The value of delta is",abs(b-a))
a = 4
b = 6
roots = []
roots.append(a)
roots.append(b)
for n in range(0,1000):
	roots.append(roots[n+1]-Bessel(M,roots[n+1])*(roots[n+1]-roots[n])/(Bessel(M,roots[n+1])-Bessel(M,roots[n])))
	if abs(Bessel(M,roots[n+2])) <= 10**-8:
		print("The root using the secant method is",roots[n+2])
		print("The value of delta is",abs(roots[n+2]-roots[n+1]))
		print("The number of iterations is",n)
		break
N = 0
while abs(Bessel(M,c)) > 10**-9:
	if Bessel(M,a)*Bessel(M,c) < 0:
		b = c
		c = (a+b)/2
		N = N + 1
	else:
		a = c
		c = (b+a)/2
		N = N + 1
	if abs(Bessel(M,c)) <= 10**-9:
		print("The root of the function using the bisection method is",c)
		print("The number of iterations is", N)
		print("The value of delta is",abs(b-a))
a = 4
b = 6
roots = []
roots.append(a)
roots.append(b)
for n in range(0,1000):
	roots.append(roots[n+1]-Bessel(M,roots[n+1])*(roots[n+1]-roots[n])/(Bessel(M,roots[n+1])-Bessel(M,roots[n])))
	if abs(Bessel(M,roots[n+2])) <= 10**-9:
		print("The root using the secant method is",roots[n+2])
		print("The value of delta is",abs(roots[n+2]-roots[n+1]))
		print("The number of iterations is",n)
		break
N = 0
while abs(Bessel(M,c)) > 10**-10:
	if Bessel(M,a)*Bessel(M,c) < 0:
		b = c
		c = (a+b)/2
		N = N + 1
	else:
		a = c
		c = (b+a)/2
		N = N + 1
	if abs(Bessel(M,c)) <= 10**-10:
		print("The root of the function using the bisection method is",c)
		print("The number of iterations is", N)
		print("The value of delta is",abs(b-a))
a = 4
b = 6
roots = []
roots.append(a)
12
roots.append(b)
for n in range(0,1000):
	roots.append(roots[n+1]-Bessel(M,roots[n+1])*(roots[n+1]-roots[n])/(Bessel(M,roots[n+1])-Bessel(M,roots[n])))
	if abs(Bessel(M,roots[n+2])) <= 10**-10:
		print("The root using the secant method is",roots[n+2])
		print("The value of delta is",abs(roots[n+2]-roots[n+1]))
		print("The number of iterations is",n)
		break
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
print("Here are the same methods on the interval [8,10].")
print()
a = 8
b = 10
c = (a+b)/2
N = 0
while abs(Bessel(M,c)) > 10**-6:
	if Bessel(M,a)*Bessel(M,c) < 0:
		b = c
		c = (a+b)/2
		N = N + 1
	else:
		a = c
		c = (b+a)/2
		N = N + 1
	if abs(Bessel(M,c)) <= 10**-6:
		print("The root of the function using the bisection method is",c)
		print("The number of iterations is", N)
		print("The value of delta is",abs(b-a))
a = 8
b = 10
roots = []
roots.append(a)
roots.append(b)
for n in range(0,1000):
	roots.append(roots[n+1]-Bessel(M,roots[n+1])*(roots[n+1]-roots[n])/(Bessel(M,roots[n+1])-Bessel(M,roots[n])))
	if abs(Bessel(M,roots[n+2])) <= 10**-6:
		print("The root using the secant method is",roots[n+2])
		print("The value of delta is",abs(roots[n+2]-roots[n+1]))
		print("The number of iterations is",n)
		break
N = 0
while abs(Bessel(M,c)) > 10**-7:
	if Bessel(M,a)*Bessel(M,c) < 0:
		b = c
		c = (a+b)/2
		N = N + 1
	else:
		a = c
		c = (b+a)/2
		N = N + 1
	if abs(Bessel(M,c)) <= 10**-7:
		print("The root of the function using the bisection method is",c)
		print("The number of iterations is", N)
		print("The value of delta is",abs(b-a))
a = 8
b = 10
roots = []
roots.append(a)
roots.append(b)
for n in range(0,1000):
	roots.append(roots[n+1]-Bessel(M,roots[n+1])*(roots[n+1]-roots[n])/(Bessel(M,roots[n+1])-Bessel(M,roots[n])))
	if abs(Bessel(M,roots[n+2])) <= 10**-7:
		print("The root using the secant method is",roots[n+2])
		print("The value of delta is",abs(roots[n+2]-roots[n+1]))
		print("The number of iterations is",n)
		break
N = 0
while abs(Bessel(M,c)) > 10**-8:
	if Bessel(M,a)*Bessel(M,c) < 0:
		b = c
		c = (a+b)/2
		N = N + 1
	else:
		a = c
		c = (b+a)/2
		N = N + 1
	if abs(Bessel(M,c)) <= 10**-8:
		print("The root of the function using the bisection method is",c)
		print("The number of iterations is", N)
		print("The value of delta is",abs(b-a))
a = 8
b = 10
roots = []
roots.append(a)
roots.append(b)
for n in range(0,1000):
	roots.append(roots[n+1]-Bessel(M,roots[n+1])*(roots[n+1]-roots[n])/(Bessel(M,roots[n+1])-Bessel(M,roots[n])))
	if abs(Bessel(M,roots[n+2])) <= 10**-8:
		print("The root using the secant method is",roots[n+2])
		print("The value of delta is",abs(roots[n+2]-roots[n+1]))
		print("The number of iterations is",n)
		break
N = 0
while abs(Bessel(M,c)) > 10**-9:
	if Bessel(M,a)*Bessel(M,c) < 0:
		b = c
		c = (a+b)/2
		N = N + 1
	else:
		a = c
		c = (b+a)/2
		N = N + 1
	if abs(Bessel(M,c)) <= 10**-9:
		print("The root of the function using the bisection method is",c)
		print("The number of iterations is", N)
		print("The value of delta is",abs(b-a))
a = 8
b = 10
roots = []
roots.append(a)
roots.append(b)
for n in range(0,1000):
	roots.append(roots[n+1]-Bessel(M,roots[n+1])*(roots[n+1]-roots[n])/(Bessel(M,roots[n+1])-Bessel(M,roots[n])))
	if abs(Bessel(M,roots[n+2])) <= 10**-9:
		print("The root using the secant method is",roots[n+2])
		print("The value of delta is",abs(roots[n+2]-roots[n+1]))
		print("The number of iterations is",n)
		break
N = 0
while abs(Bessel(M,c)) > 10**-10:
	if Bessel(M,a)*Bessel(M,c) < 0:
		b = c
		c = (a+b)/2
		N = N + 1
	else:
		a = c
		c = (b+a)/2
		N = N + 1
	if abs(Bessel(M,c)) <= 10**-10:
		print("The root of the function using the bisection method is",c)
		print("The number of iterations is", N)
		print("The value of delta is",abs(b-a))
a = 8
b = 10
roots = []
roots.append(a)
roots.append(b)
for n in range(0,1000):
	roots.append(roots[n+1]-Bessel(M,roots[n+1])*(roots[n+1]-roots[n])/(Bessel(M,roots[n+1])-Bessel(M,roots[n])))
	if abs(Bessel(M,roots[n+2])) <= 10**-10:
		print("The root using the secant method is",roots[n+2])
		print("The value of delta is",abs(roots[n+2]-roots[n+1]))
		print("The number of iterations is",n)
		break

