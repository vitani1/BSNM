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
"""
Task 1
Interpolate f(x) with a polynomial p(x) of degree n using
equidistant points x_i between -1 and 1, such that x_i = (2i/n)-1
for i = 0, 1, ....., n. Use the code
to interpolate f(x) with n = 6, 10, 14, and 18 for the values of
c = 1, 4, and 25. For each value of c, plot in the same graph the
function f(x) and its
interpolating polynomial with n = 6, 10, 14, and 18. Plot for
each c the graph of the error e(x) = || f(x)-p(x) || for n = 6,
10, 14, and 18. 
"""
def f(x,c):
	return 1/(c*x**2+1)
def lagrange(x,nodes,n,function):
	f = 0
	for i in range(0,n):
		l = 1
		for j in range(0,n):
			if i != j:
				l = l*(x-nodes[j])/(nodes[i]-nodes[j])
		f = f+l*function[i]
	return f
# n = 6, c = 1
c = 1
n = 6
error = np.zeros(n)
nodes = np.zeros(n)
function = np.zeros(n)
for i in range(0,n):
	nodes[i] = (2*i/(n-1))-1
for i in range(0,len(function)):
	function[i] = f(nodes[i],c)
print(nodes)
print("Here is a graph of the interpolated function using c = 1 and n = 6.")
x = linspace(-1,1,100)
y = lagrange(x,nodes,n,function)
plot(x,y)
plt.xlabel('x')
plt.ylabel('p(x)')
plt.savefig('c=1,n=6')
plt.show()
print("Here is a graph of the error between the actual function values and the polynomial using c = 1 and n = 6:")
x = linspace(-1,1,100)
y = abs(f(x,c)-lagrange(x,nodes,n,function))
plot(x,y)
plt.xlabel('x')
plt.ylabel('error')
plt.savefig('c=1,n=6 error')
show()
print("Here is a graph of the interpolated function using c = 4 and n = 6.")
#n = 6, c = 4
c = 4
function = np.zeros(n)
for i in range(0,len(function)):
	function[i] = f(nodes[i],c)
x = linspace(-1,1,100)
y = lagrange(x,nodes,n,function)
plot(x,y)
plt.xlabel('x')
plt.ylabel('p(x)')
plt.savefig('c=4,n=6')
show()
print("Here is a graph of the error between the actual function values and the polynomial using c = 4 and n = 6:")
x = linspace(-1,1,100)
y = abs(f(x,c)-lagrange(x,nodes,n,function))
plot(x,y)
plt.xlabel('x')
plt.ylabel('error')
plt.savefig('c=4,n=6 error')
show()
print("Here is a graph of the interpolated function using c = 25 and n = 6.")
#n = 6, c = 25
c = 25
function = np.zeros(n)
for i in range(0,len(function)):
	function[i] = f(nodes[i],c)
x = linspace(-1,1,100)
y = lagrange(x,nodes,n,function)
plot(x,y)
plt.xlabel('x')
plt.ylabel('p(x)')
plt.savefig('c=25,n=6')
show()
print("Here is a graph of the error between the actual function values and the polynomial using c = 25 and n = 6:")
x = linspace(-1,1,100)
y = abs(f(x,c)-lagrange(x,nodes,n,function))
plot(x,y)
plt.xlabel('x')
plt.ylabel('error')
plt.savefig('c=25,n=6')
show()
#n = 10, c = 1
c = 1
n = 10
nodes = np.zeros(n)
function = np.zeros(n)
for i in range(0,len(nodes)):
	nodes[i] = (2*i/(n-1))-1
for i in range(0,len(function)):
	function[i] = f(nodes[i],c)
print("Here is a graph of the interpolated function using c = 1 and n = 10.")
x = linspace(-1,1,100)
y = lagrange(x,nodes,n,function)
plot(x,y)
plt.xlabel('x')
plt.ylabel('p(x)')
show()
print("Here is a graph of the error between the actual function values and the polynomial using c = 1 and n = 10:")
x = linspace(-1,1,100)
y = abs(f(x,c)-lagrange(x,nodes,n,function))
plot(x,y)
plt.xlabel('x')
plt.ylabel('error')
show()
print("Here is a graph of the interpolated function using c = 4 and n = 10.")
#n = 10, c = 4
c = 4
function = np.zeros(n)
for i in range(0,len(function)):
	function[i] = f(nodes[i],c)
x = linspace(-1,1,100)
y = lagrange(x,nodes,n,function)
plot(x,y)
plt.xlabel('x')
plt.ylabel('p(x)')
show()
print("Here is a graph of the error between the actual function values and the polynomial using c = 4 and n = 10:")
x = linspace(-1,1,100)
y = abs(f(x,c)-lagrange(x,nodes,n,function))
plot(x,y)
plt.xlabel('x')
plt.ylabel('error')
show()
print("Here is a graph of the interpolated function using c = 25 and n = 10.")
#c = 25, n = 10
c = 25
function = np.zeros(n)
for i in range(0,len(function)):
	function[i] = f(nodes[i],c)
x = linspace(-1,1,100)
y = lagrange(x,nodes,n,function)
plot(x,y)
plt.xlabel('x')
plt.ylabel('p(x)')
show()
print("Here is a graph of the error between the actual function values and the polynomial using c = 25 and n = 10:")
x = linspace(-1,1,100)
y = abs(f(x,c)-lagrange(x,nodes,n,function))
plot(x,y)
plt.xlabel('x')
plt.ylabel('error')
show()
# n = 14, c = 1
c = 1
n = 14
nodes = np.zeros(n)
function = np.zeros(n)
for i in range(0,len(nodes)):
	nodes[i] = (2*i/(n-1))-1
for i in range(0,len(function)):
	function[i] = f(nodes[i],c)
print("Here is a graph of the interpolated function using c = 1 and n = 14.")
x = linspace(-1,1,100)
y = lagrange(x,nodes,n,function)
plot(x,y)
plt.xlabel('x')
plt.ylabel('p(x)')
show()
print("Here is a graph of the error between the actual function values and the polynomial using c = 1 and n = 14:")
x = linspace(-1,1,100)
y = abs(f(x,c)-lagrange(x,nodes,n,function))
plot(x,y)
plt.xlabel('x')
plt.ylabel('error')
show()
print("Here is a graph of the interpolated function using c = 4 and n = 14.")
# n = 14, c = 4
c = 4
function = np.zeros(n)
for i in range(0,len(function)):
	function[i] = f(nodes[i],c)
x = linspace(-1,1,100)
y = lagrange(x,nodes,n,function)
plot(x,y)
plt.xlabel('x')
plt.ylabel('p(x)')
show()
print("Here is a graph of the error between the actual function values and the polynomial using c = 4 and n = 14:")
x = linspace(-1,1,100)
y = abs(f(x,c)-lagrange(x,nodes,n,function))
plot(x,y)
plt.xlabel('x')
plt.ylabel('error')
show()
print("Here is a graph of the interpolated function using c = 25 and n = 14.")
# n = 14, c = 25
c = 25
function = np.zeros(n)
for i in range(0,len(function)):
	function[i] = f(nodes[i],c)
x = linspace(-1,1,100)
y = lagrange(x,nodes,n,function)
plot(x,y)
plt.xlabel('x')
plt.ylabel('p(x)')
show()
print("Here is a graph of the error between the actual function values and the polynomial using c = 25 and n = 14:")
x = linspace(-1,1,100)
y = abs(f(x,c)-lagrange(x,nodes,n,function))
plot(x,y)
plt.xlabel('x')
plt.ylabel('error')
show()
# n = 18, c = 1
c = 1
n = 18
nodes = np.zeros(n)
function = np.zeros(n)
for i in range(0,len(nodes)):
	nodes[i] = (2*i/(n-1))-1
for i in range(0,len(function)):
	function[i] = f(nodes[i],c)
print("Here is a graph of the interpolated function using c = 1 and n = 18.")
x = linspace(-1,1,100)
y = lagrange(x,nodes,n,function)
plot(x,y)
plt.xlabel('x')
plt.ylabel('p(x)')
show()
print("Here is a graph of the error between the actual function values and the polynomial using c = 1 and n = 18:")
x = linspace(-1,1,100)
y = abs(f(x,c)-lagrange(x,nodes,n,function))
plot(x,y)
plt.xlabel('x')
plt.ylabel('error')
show()
print("Here is a graph of the interpolated function using c = 4 and n = 18.")
#n = 18, c = 4
c = 4
function = np.zeros(n)
for i in range(0,len(function)):
	function[i] = f(nodes[i],c)
x = linspace(-1,1,100)
y = lagrange(x,nodes,n,function)
plot(x,y)
plt.xlabel('x')
plt.ylabel('p(x)')
show()
print("Here is a graph of the error between the actual function values and the polynomial using c = 4 and n = 18:")
x = linspace(-1,1,100)
y = abs(f(x,c)-lagrange(x,nodes,n,function))
plot(x,y)
plt.xlabel('x')
plt.ylabel('error')
show()
print("Here is a graph of the interpolated function using c = 25 and n = 18.")
# n = 18, c = 25
c = 25
function = np.zeros(n)
for i in range(0,len(function)):
	function[i] = f(nodes[i],c)
x = linspace(-1,1,100)
y = lagrange(x,nodes,n,function)
plot(x,y)
plt.xlabel('x')

plt.ylabel('p(x)')
show()
print("Here is a graph of the error between the actual function values and the polynomial using c = 25 and n = 18:")
x = linspace(-1,1,100)
y = abs(f(x,c)-lagrange(x,nodes,n,function))
plot(x,y)
plt.xlabel('x')
plt.ylabel('error')
show()
"""
The same procedure will be used with nodes x = cos((2i-1)*pi/2n)
"""
print("The same procedure will be used with nodes x = cos((2i-1)*pi/2n)")
# n = 6
# c = 1
c = 1
n = 6
error = np.zeros(n)
nodes = np.zeros(n)
function = np.zeros(n)
for i in range(1,n):
	nodes[i] = cos(((2*i-1)*pi)/(2*n))
for i in range(0,len(function)):
	function[i] = f(nodes[i],c)
print("Here is a graph of the interpolated function using c = 1 and n = 6.")
x = linspace(nodes[0],nodes[n-1],100)
y = lagrange(x,nodes,n,function)
plot(x,y)
plt.xlabel('x')
plt.ylabel('p(x)')
show()
print("Here is a graph of the error between the actual function values and the polynomial using c = 1 and n = 6:")
x = linspace(nodes[0],nodes[n-1],100)
y = abs(f(x,c)-lagrange(x,nodes,n,function))
plot(x,y)
plt.xlabel('x')
plt.ylabel('error')
show()
print("Here is a graph of the interpolated function using c = 4 and n = 6.")
# n = 6, c = 4
c = 4
function = np.zeros(n)
nodes = np.zeros(n)
for i in range(1,n):
	nodes[i] = cos(((2*i-1)*pi)/(2*n))
for i in range(0,len(function)):
	function[i] = f(nodes[i],c)
x = linspace(nodes[0],nodes[n-1],100)
y = lagrange(x,nodes,n,function)
plot(x,y)
plt.xlabel('x')
plt.ylabel('p(x)')
show()
print("Here is a graph of the error between the actual function values and the polynomial using c = 4 and n = 6:")
x = linspace(nodes[0],nodes[n-1],100)
y = abs(f(x,c)-lagrange(x,nodes,n,function))
plot(x,y)
plt.xlabel('x')
plt.ylabel('error')
show()
print("Here is a graph of the interpolated function using c = 25 and n = 6.")
# n = 6, c = 25
c = 25
function = np.zeros(n)
for i in range(0,len(function)):
	function[i] = f(nodes[i],c)
x = linspace(nodes[0],nodes[n-1],100)
y = lagrange(x,nodes,n,function)
plot(x,y)
plt.xlabel('x')
plt.ylabel('p(x)')
show()
print("Here is a graph of the error between the actual function values and the polynomial using c = 25 and n = 6:")
x = linspace(nodes[0],nodes[n-1],100)
y = abs(f(x,c)-lagrange(x,nodes,n,function))
plot(x,y)
plt.xlabel('x')
plt.ylabel('error')
show()
# n = 10, c = 1
c = 1
n = 10
function = np.zeros(n)
nodes = np.zeros(n)
for i in range(1,n):
	nodes[i] = cos(((2*i-1)*pi)/(2*n))
for i in range(0,len(function)):
	function[i] = f(nodes[i],c)
print("Here is a graph of the interpolated function using c = 1 and n = 10.")
x = linspace(nodes[0],nodes[n-1],100)
y = lagrange(x,nodes,n,function)
plot(x,y)
plt.xlabel('x')
plt.ylabel('p(x)')
show()
print("Here is a graph of the error between the actual function values and the polynomial using c = 1 and n = 10:")
x = linspace(nodes[0],nodes[n-1],100)
y = abs(f(x,c)-lagrange(x,nodes,n,function))
plot(x,y)
plt.xlabel('x')
plt.ylabel('error')
show()
print("Here is a graph of the interpolated function using c = 4 and n = 10.")
# n = 10, c = 4
c = 4
function = np.zeros(n)
for i in range(0,len(function)):
	function[i] = f(nodes[i],c)
x = linspace(nodes[0],nodes[n-1],100)
y = lagrange(x,nodes,n,function)
plot(x,y)
plt.xlabel('x')
plt.ylabel('p(x)')
show()
print("Here is a graph of the error between the actual function values and the polynomial using c = 4 and n = 10:")
x = linspace(nodes[0],nodes[n-1],100)
y = abs(f(x,c)-lagrange(x,nodes,n,function))
plot(x,y)
plt.xlabel('x')
plt.ylabel('error')
show()
print("Here is a graph of the interpolated function using c = 25 and n = 10.")
# n = 10, c = 25
c = 25
function = np.zeros(n)
for i in range(0,len(function)):
	function[i] = f(nodes[i],c)
x = linspace(nodes[0],nodes[n-1],100)
y = lagrange(x,nodes,n,function)
plot(x,y)
plt.xlabel('x')
plt.ylabel('p(x)')
show()
print("Here is a graph of the error between the actual function values and the polynomial using c = 25 and n = 10:")
x = linspace(nodes[0],nodes[n-1],100)
y = abs(f(x,c)-lagrange(x,nodes,n,function))
plot(x,y)
plt.xlabel('x')
plt.ylabel('error')
show()
# n = 14, c = 1
c = 1
n = 14
nodes = np.zeros(n)
for i in range(1,n):
	nodes[i] = cos(((2*i-1)*pi)/(2*n))
function = np.zeros(n)
for i in range(0,len(function)):
	function[i] = f(nodes[i],c)
print("Here is a graph of the interpolated function using c = 1 and n = 14.")
x = linspace(nodes[0],nodes[n-1],100)
y = lagrange(x,nodes,n,function)
plot(x,y)
plt.xlabel('x')
plt.ylabel('p(x)')
show()
print("Here is a graph of the error between the actual function values and the polynomial using c = 1 and n = 14:")
x = linspace(nodes[0],nodes[n-1],100)
y = abs(f(x,c)-lagrange(x,nodes,n,function))
plot(x,y)
plt.xlabel('x')
plt.ylabel('error')
show()
print("Here is a graph of the interpolated function using c = 4 and n = 14.")
# n = 14, c = 4
c = 4
function = np.zeros(n)
for i in range(0,len(function)):
	function[i] = f(nodes[i],c)
x = linspace(nodes[0],nodes[n-1],100)
y = lagrange(x,nodes,n,function)
plot(x,y)
plt.xlabel('x')
plt.ylabel('p(x)')
show()
print("Here is a graph of the error between the actual function values and the polynomial using c = 4 and n = 14:")
x = linspace(nodes[0],nodes[n-1],100)
y = abs(f(x,c)-lagrange(x,nodes,n,function))
plot(x,y)
plt.xlabel('x')
plt.ylabel('error')
show()
print("Here is a graph of the interpolated function using c = 25 and n = 14.")
# n = 14, c = 25
c = 25
function = np.zeros(n)
for i in range(0,len(function)):
	function[i] = f(nodes[i],c)
x = linspace(nodes[0],nodes[n-1],100)
y = lagrange(x,nodes,n,function)
plot(x,y)
plt.xlabel('x')
plt.ylabel('p(x)')
show()
print("Here is a graph of the error between the actual function values and the polynomial using c = 25 and n = 14:")
x = linspace(nodes[0],nodes[n-1],100)
y = abs(f(x,c)-lagrange(x,nodes,n,function))
plot(x,y)
plt.xlabel('x')
plt.ylabel('error')
show()
# n = 18, c = 1
c = 1
n = 18
nodes = np.zeros(n)
for i in range(1,n):
	nodes[i] = cos(((2*i-1)*pi)/(2*n))
function = np.zeros(n)
for i in range(0,len(function)):
	function[i] = f(nodes[i],c)
print("Here is a graph of the interpolated function using c = 1 and n = 18.")
x = linspace(nodes[0],nodes[n-1],100)
y = lagrange(x,nodes,n,function)
plot(x,y)
plt.xlabel('x')
plt.ylabel('p(x)')
show()
print("Here is a graph of the error between the actual function values and the polynomial using c = 1 and n = 18:")
x = linspace(nodes[0],nodes[n-1],100)
y = abs(f(x,c)-lagrange(x,nodes,n,function))
plot(x,y)
plt.xlabel('x')
plt.ylabel('error')
show()
print("Here is a graph of the interpolated function using c = 4 and n = 18.")
# n = 18, c = 4
c = 4
function = np.zeros(n)
for i in range(0,len(function)):
	function[i] = f(nodes[i],c)
x = linspace(nodes[0],nodes[n-1],100)
y = lagrange(x,nodes,n,function)
plot(x,y)
plt.xlabel('x')
plt.ylabel('p(x)')
show()
print("Here is a graph of the error between the actual function values and the polynomial using c = 4 and n = 18:")
x = linspace(nodes[0],nodes[n-1],100)
y = abs(f(x,c)-lagrange(x,nodes,n,function))
plot(x,y)
plt.xlabel('x')
plt.ylabel('error')
show()
print("Here is a graph of the interpolated function using c = 25 and n = 18.")
# n = 18, c = 25
c = 25
function = np.zeros(n)
for i in range(0,len(function)):
	function[i] = f(nodes[i],c)
x = linspace(nodes[0],nodes[n-1],100)
y = lagrange(x,nodes,n,function)
plot(x,y)
plt.xlabel('x')
plt.ylabel('p(x)')
show()
print("Here is a graph of the error between the actual function values and the polynomial using c = 25 and n = 18:")
x = linspace(nodes[0],nodes[n-1],100)
y = abs(f(x,c)-lagrange(x,nodes,n,function))
plot(x,y)
plt.xlabel('x')
plt.ylabel('error')
show()
