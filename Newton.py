import numpy as np
import math
import matplotlib as npl
import scipy.special
from numpy import abs,sin,cos,e,linspace,pi
from pylab import plot,show,savefig,xlabel,ylabel
from matplotlib import pyplot as plt
def f1(x):
	return sin(3*x) * e**-x
def f1deriv(x):
	return (-e**(-x))*sin(3*x)+3*cos(3*x)*e**(-x)
delta = 10**-16
a = 0
b = 10
error = []
iterations = []
x = linspace(a,b,100)
print("The function is sin(3x)e^(-x).")
print("Newton's Method will now be performed on the interval [0,10] using the midpoint of the interval as the initial starting value.")
x = (a+b)/2 #The first point in Newton's Method will be the midpoint.
N = 0
points = []
points.append(x)
error = []
iterations = []
epsilon = 10**-6
for i in range(1,1000):
	x = x - f1(x)/f1deriv(x)
	points.append(x)
	N = N + 1
	iterations.append(N)
	error.append(abs(x-points[i-1]))
	if abs(f1(x)) <= epsilon:
		print("The value of the root using Newton's Method using epsilon = 10^-6 is",x)
		print("The number of iterations is",N)
		plot(iterations,error)
		xlabel('Iterations')
		ylabel('Delta')
		show()
		break
x = (a+b)/2 #The first point in Newton's Method will be the midpoint.
N = 0
points = []
error = []
iterations = []
points.append(x)
epsilon = 10**-7
for i in range(1,1000):
	x = x - f1(x)/f1deriv(x)
	points.append(x)
	N = N + 1
	iterations.append(N)
	error.append(abs(x-points[i-1]))
	if abs(f1(x)) <= epsilon:
		print("The value of the root using Newton's Method using epsilon = 10^-7 is",x)
		print("The number of iterations is",N)
		plot(iterations,error)
		xlabel('Iterations')
		ylabel('Delta')
		show()
		break
x = (a+b)/2 #The first point in Newton's Method will be the midpoint.
N = 0
points = []
error = []
iterations = []
points.append(x)
epsilon = 10**-8
for i in range(1,1000):
	x = x - f1(x)/f1deriv(x)
	points.append(x)
	N = N + 1
	iterations.append(N)
	error.append(abs(x-points[i-1]))
	if abs(f1(x)) <= epsilon:
		print("The value of the root using Newton's Method using epsilon = 10^-8 is",x)
		print("The number of iterations is",N)
		plot(iterations,error)
		xlabel('Iterations')
		ylabel('Delta')
		show()
		break
x = (a+b)/2 #The first point in Newton's Method will be the midpoint.
N = 0
points = []
error = []
iterations = []
points.append(x)
epsilon = 10**-9
for i in range(1,1000):
	x = x - f1(x)/f1deriv(x)
	points.append(x)
	N = N + 1
	iterations.append(N)
	error.append(abs(x-points[i-1]))
	if abs(f1(x)) <= epsilon:	
		print("The value of the root using Newton's Method using epsilon = 10^-9 is",x)
		print("The number of iterations is",N)
		plot(iterations,error)
		xlabel('Iterations')
		ylabel('Delta')
		show()
		break
x = (a+b)/2 #The first point in Newton's Method will be the midpoint.
N = 0
points = []
error = []
iterations = []
points.append(x)
epsilon = 10**-10
for i in range(1,1000):
	x = x - f1(x)/f1deriv(x)
	points.append(x)
	N = N + 1
	iterations.append(N)
	error.append(abs(x-points[i-1]))
	if abs(f1(x)) <= epsilon:
		print("The value of the root using Newton's Method using epsilon = 10^-10 is",x)
		print("The number of iterations is",N)
		plot(iterations,error)
		xlabel('Iterations')
		ylabel('Delta')
		show()
		break 

