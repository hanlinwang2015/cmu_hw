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
plt.show()
def getiput():
	x = sp.symbols('x')
	y = sp.symbols('y')
	a = sp.Matrix([[2, 0, 2 * y * y - 1, 0], [0, 2, 0, 2 * y * y - 1], [1, 1 + 2 * y, y * y - y, 0], [0, 1, 1 + 2 * y, y * y - y]])
	print(sp.solve(a.det(), y))
	print(sp.factor(a.det()))
getiput()
