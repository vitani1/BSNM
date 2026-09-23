import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.special
from numpy import sin,cos,e

def f(x):
	f = sin(3*x)*e**-x
	return f
x=np.linspace(0,10)
plt.plot(x,f(x))
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
