import numpy as np
import math
import matplotlib as npl
from numpy import abs,sin,cos,e,linspace,pi,append
from pylab import plot,show,savefig,xlabel,ylabel
from matplotlib import pyplot as plt

def f(x):
	s = x**3-2*x*x+6*x-1
	return s
x = np.linspace(-10,10)
x_1 = np.linspace(-10,-5)
#x_2 = np.linspace(-5,0)
x_2 = np.linspace(-5,5)
#x_3 = np.linspace(0,5)
x_4 = np.linspace(5,10)

#def Spline1(x):
#	s = -1255-27*(x+10)**2+346*(x+10)
#	return s
#def Spline2(x):
#	s = -200+76*(x+5)-(181/25)*(x+5)**2
#	return s
#def Spline3(x):
#	s = -1 + (18/5)*x+103*x*x/25
#	return s
#def Spline4(x):
#	s = 120+(224/5)*(x-5)+(523/25)*(x-5)**2
#	return s
#plt.plot(x,f(x),label = 'Original function')
#plt.plot(x_1,Spline1(x_1),label = 'Spline 1 : [-10,-5]')
#plt.plot(x_2,Spline2(x_2), label = 'Spline 2: [-5,0]')
#plt.plot(x_3,Spline3(x_3), label = 'Spline 3: [0,5]')
#plt.plot(x_4,Spline4(x_4), label = 'Spline 4: [5,10]')
#plt.legend()
#plt.title("Quadratic Splines")
#plt.xlabel("x")
#plt.ylabel("y")
#plt.show()
#plt.plot(x_1,np.abs(Spline1(x_1)-f(x)), label = '|Spline 1 - f(x)| : [-10,-5]')
#plt.plot(x_2,np.abs(Spline2(x_2)-f(x)), label = '|Spline 2 - f(x)| : [-5,0]')
#plt.plot(x_3,np.abs(Spline3(x_3)-f(x)), label = '|Spline 3 - f(x)| : [0,5]')
#plt.plot(x_4,np.abs(Spline4(x_4)-f(x)), label = '|Spline 4 - f(x)| : [5,10]')
#plt.legend()
#plt.title("Error between actual function and splines graphed in each domain")
#plt.xlabel("x")
#plt.ylabel("y")
#plt.show()
#Cubic Spline

def Spline1(x):
	s = -1255 + 346*(x+10)-32.14*(x+10)**2+1.0281*(x+10)**3
	return s
def Spline2(x):
	s = -200 +101.702*(x+5)-16.719*(x+5)**2+0.9749*(x+5)**3
	return s
def Spline3(x):
	s = 120 + 59.7816*(x-5) + 12.5274*(x-5)**2+1.0793*(x-5)**3
	return s
plt.plot(x,f(x),label = 'Original function')
plt.plot(x_1,Spline1(x_1),label = 'Spline 1 : [-10,-5]')
plt.plot(x_2,Spline2(x_2), label = 'Spline 2: [-5,5]')
plt.plot(x_4,Spline3(x_4), label = 'Spline 3: [5,10]')
plt.legend()
plt.title("Cubic Splines")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
plt.plot(x_1,np.abs(Spline1(x_1)-f(x)), label = '|Spline 1 - f(x)| : [-10,-5]')
plt.plot(x_2,np.abs(Spline2(x_2)-f(x)), label = '|Spline 2 - f(x)| : [-5,5]')
plt.plot(x_4,np.abs(Spline3(x_4)-f(x)), label = '|Spline 3 - f(x)| : [5,10]')
plt.legend()
plt.title("Error between actual function and splines graphed in each domain")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
