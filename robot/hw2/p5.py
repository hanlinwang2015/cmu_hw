#! /usr/bin/python
import math
def newton(initial):
	iterate = 0
	xx = initial
	while abs(math.tan(xx)) > 0.01 and iterate < 10000:
		xx -= math.tan(xx) * pow(math.cos(xx), 2)
		iterate += 1
	if math.tan(xx) > 0.01:
		print("bad initial guess, try again")
	else:
		print("the solution:", xx)
		
	
newton(5)
