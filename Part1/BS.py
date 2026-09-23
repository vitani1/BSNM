import numpy as np
import math
import matplotlib as npl
import scipy.special
from numpy import abs,sin,cos,e,linspace,pi
from pylab import plot,show,savefig,xlabel,ylabel
from matplotlib import pyplot as plt

def f(x):
	s = x*x-2*x+1
	return s
x = np.linspace(-2,5)
plt.plot(x,f(x))
plt.xlabel("x")
plt.ylabel("y")
plt.show()
