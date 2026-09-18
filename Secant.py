#Secant Method
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.special
from numpy import sin,cos
def Secant(x,y):
	return x - f(x)*(x-y)/(f(x)-f(y))
def polynomial(x,a0,a1,a2,a3,a4):
	return a0 + a1*x + a2*x**2 + a3*x**3 + a4*x**4
delta = 10**-16
print("The program will use the secant method on a basic fourth-degree polynomial to test that it works.")
n = 4
print("The chosen test function is 4x^4-7x^3+x^2-1 in the interval [-2,2]")
#a = float(input("Please input a number for the left side of the interval."))
#b = float(input("Please input a number for the right ride of the interval."))
a = -2
b = 2
c = (a+b)/2
N = 0
a0 = -1
a1 = 0
a2 = 1
a3 = -7
a4 = 4
while abs(b-a) > delta:
	if polynomial(a,a0,a1,a2,a3,a4)*polynomial(c,a0,a1,a2,a3,a4) < 0:
		b = c
		c = (a+b)/2
		N = N+1
	else:
		a = c
		c = (b+a)/2
		N = N+1
	if abs(b-a)<=delta:
		print("The root of the function is",c)
		print("The value of epsilon is",abs(polynomial(c,a0,a1,a2,a3,a4)))
		print("The number of iterations is",N)
roots = []
print("Please enter in two starting values for the secant method.")
roots.append(float(input()))
roots.append(float(input()))
for n in range(0,1000):
	roots.append(roots[n+1]-polynomial(roots[n+1],a0,a1,a2,a3,a4)*(roots[n+1]-roots[n])/(polynomial(roots[n+1],a0,a1,a2,a3,a4)-polynomial(roots[n],a0,a1,a2,a3,a4)))
	if abs(roots[n+2]-roots[n+1])<=delta:
		print("The root using the secant method is",roots[n+2])
		print("The value of epsilon is", abs(polynomial(roots[n+2],a0,a1,a2,a3,a4)))
		print("The number of iterations is",n)
		break
x = np.linspace(-10,10)
plt.plot(x,polynomial(x,-1,0,1,-7,4))
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
plt.save("Secant.jpg")
