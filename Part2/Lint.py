"""
Consider the function f(x) = 1/(cx^2+1) where c is a positive
real number.
"""
import numpy as np
import math
import matplotlib as npl
from numpy import abs,sin,cos,e,linspace,pi,append
from pylab import plot,show,savefig,xlabel,ylabel
from matplotlib import pyplot as plt

def f(x,c):
	s = 1/(c*x**2+1)
	return s
x = np.linspace(-1,1)
for c in [1,4,25]:
	plt.plot(x,f(x,c))
	plt.xlabel("x")
	plt.ylabel("p(x)")
plt.show()
