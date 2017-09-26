#! /usr/bin/python

import sympy as sp

def getiput():
	x = sp.symbols('x')
	y = sp.symbols('y')
	a = sp.Matrix([[2, 0, 2 * y * y - 1, 0], [0, 2, 0, 2 * y * y - 1], [1, 1 + 2 * y, y * y - y, 0], [0, 1, 1 + 2 * y, y * y - y]])
	print(sp.solve(a.det(), y))
	print(sp.factor(a.det()))
getiput()
