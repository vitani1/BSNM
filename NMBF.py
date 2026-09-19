import numpy as np
import math
import matplotlib as npl
import scipy.special
from numpy import abs,sin,cos,e,linspace,pi
from pylab import plot,show,savefig,xlabel,ylabel
from matplotlib import pyplot as plt

print("Newton's Method will now be performed using initial value x = 10 for epsilon = 10^-6, 10^-7, 10^-8, 10^-9, 10^-10:")
N = 40
M = 0
x = 9
epsilon = 10**-6
for i in range(0,1000):
	J = np.zeros(N+1)
	J[N-1] = 1
	for n in range (N,1,-1):
		J[n-2] = float(((2*(n-1))/x)*J[n-1]-J[n])
	y = J[0]
	for i in range(2,N,2):
		y = y + 2*J[i]
	Jnorm = J/y
	x = x + Jnorm[0]/Jnorm[1]
	M = M + 1
	if abs(Jnorm[0]) <= epsilon:
		print("The value of the root using Newton's Method using epsilon = 10^-6 is",x)
		print("The number of iterations is",M)
		break
x = 9
M = 0
epsilon = 10**-7
for i in range(0,1000):
	J = np.zeros(N+1)
	J[N-1] = 1
	for n in range (N,1,-1):
		J[n-2] = float(((2*(n-1))/x)*J[n-1]-J[n])
	y = J[0]
	for i in range(2,N,2):
		y = y + 2*J[i]
	Jnorm = J/y
	x = x + Jnorm[0]/Jnorm[1]
	M = M + 1
	if abs(Jnorm[0]) <= epsilon:
		print("The value of the root using Newton's Method using epsilon = 10^-7 is",x)
		print("The number of iterations is",M)
		break
x = 9
M = 0
epsilon = 10**-8
for i in range(0,1000):
	J = np.zeros(N+1)
	J[N-1] = 1
	for n in range (N,1,-1):
		J[n-2] = float(((2*(n-1))/x)*J[n-1]-J[n])
	y = J[0]
	for i in range(2,N,2):
		y = y + 2*J[i]
	Jnorm = J/y
	x = x + Jnorm[0]/Jnorm[1]
	M = M + 1
	if abs(Jnorm[0]) <= epsilon:
		print("The value of the root using Newton's Method using epsilon = 10^-8 is",x)
		print("The number of iterations is",M)
		break
x = 9
M = 0
epsilon = 10**-9
for i in range(0,1000):
	J = np.zeros(N+1)
	J[N-1] = 1
	for n in range (N,1,-1):
		J[n-2] = float(((2*(n-1))/x)*J[n-1]-J[n])
	y = J[0]
	for i in range(2,N,2):
		y = y + 2*J[i]
	Jnorm = J/y
	x = x + Jnorm[0]/Jnorm[1]
	M = M + 1
	if abs(Jnorm[0]) <= epsilon:
		print("The value of the root using Newton's Method using epsilon = 10^-9 is",x)
		print("The number of iterations is",M)
		break
x = 9
M = 0
epsilon = 10**-10
for i in range(0,1000):
	J = np.zeros(N+1)
	J[N-1] = 1
	for n in range (N,1,-1):
		J[n-2] = float(((2*(n-1))/x)*J[n-1]-J[n])
	y = J[0]
	for i in range(2,N,2):
		y = y + 2*J[i]
	Jnorm = J/y
	x = x + Jnorm[0]/Jnorm[1]
	M = M + 1
	if abs(Jnorm[0]) <= epsilon:
		print("The value of the root using Newton's Method using epsilon = 10^-10 is",x)
		print("The number of iterations is",M)
		break

