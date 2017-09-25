#! /usr/bin/python
import cmath

import math
roots=[]
def gen(x):
	if len(roots) == 0:
		return pow(x, 3) - 4 * pow(x, 2) + 6 * x - 4
	else:
		temp =  pow(x, 3) - 4 * pow(x, 2) + 6 * x - 4
		for i in roots:
			temp = temp / (x - i)
		return temp
def muller(x1, x2, x3):
	rootcount = 0
	c1 = x1
	c2 = x2
	c3 = x3
	count = 0
	while len(roots) < 3:
		x1 = c1
		x2 = c2
		x3 = c3	
		count = 0
		while count < 1000000 and (abs(x1 - x2) > 0.001 or abs(x2 - x3) > 0.001):
			count += 1
			f1 = gen(x1)
			f2 = gen(x2)
			f3 = gen(x3)

			c = f3
			h1 = x2 - x1
			h2 = x3 - x2
			d0 = (f2 - f1) / h1
			d1 = (f3 - f2) / h2
			a = (d1 - d0) / (h1 + h2)
			b = a * h2 + d1
			cc = (b * b - 4 * a * c) 
			temp =cmath.sqrt(cc)
			if abs(b - temp) >= abs(b + temp):
				den = b - temp
			else:
				den = b + temp
			dxr = -2 * c / den
			xr = x3 + dxr
			x1 = x2
			x2 = x3
			x3 = xr
		if len(roots) > 0:
			dual = 0
			for j in roots:
				if abs(j - x2) < 0.000001:
					dual = 1
			if dual == 0:
				roots.append(x2)
				if abs(x2.imag)> 0.0000000001:
					roots.append(x2.conjugate())
		else:
			roots.append(x2)
			if abs(x2.imag)> 0.0000000001:
				roots.append(x2.conjugate())


				

muller(-1.5, 0.0, 1.235)
print(roots)
		
		
	
