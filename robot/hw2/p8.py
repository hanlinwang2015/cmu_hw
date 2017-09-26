#! /usr/bin/python

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1.0, 1.0, 1000)
y = np.linspace(-1.0, 1.0, 1000)
X, Y = np.meshgrid(x,y)
F = 2 * X**2 + 2 * Y**2 - 1.0
F1 = X ** 2 + Y ** 2 + 2 * X * Y + X - Y
plt.contour(X,Y,F,[0])

plt.contour(X,Y,F1,[0])
#plt.show()
def getiput():
	x = sp.symbols('x')
	y = sp.symbols('y')
	a = sp.Matrix([[2, 0, 2 * x**2  - 1, 0], [0, 2, 0, 2 * x * x - 1], [1, -1 + 2 * x, x * x + x, 0], [0, 1, -1 + 2 * x, x * x + x]])
	print(a.det())
	print(sp.solve(a.det(), x, real=True))
#	print(sp.solve([2 * x**2 + 2 * y**2 - 1, x**2 + y**2 + 2 * x * y + x - y], dict=True))
getiput()
x1 = (1 - 5.0**0.5) / 4 + ((5.0**0.5 - 1.0) / 8)**0.5
y1 = (5.0**0.5 - 1) / 4 + (((5.0**0.5 - 1.0) / 8)**0.5)

plt.scatter(x1, 0.0)

x2 = (1 - 5.0**0.5) / 4 - ((5.0**0.5 - 1) / 8)**0.5,

y2 = (5.0**0.5 - 1) / 4 - (((5.0**0.5 - 1.0) / 8)**0.5)


plt.scatter(x2, 0.0)
plt.show()
