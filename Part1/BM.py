import numpy as np
import math
import scipy.special
import matplotlib.pyplot as plt
from numpy import sin,cos
def p(x):
	f = -2 + x + 2*x*x
	return f
a = float(input("Please enter a number for the left side of the interval."))
b = float(input("Please enter a number for the right side of the interval."))
x = np.linspace(a,b,100)
plt.plot(x,p(x))
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
