#! /usr/bin/python
import math

def newton(initial):
	iterate = 0
	xx = initial
	while abs(math.cos(xx) * xx - math.sin(xx)) > 0.000001 and iterate < 10000000:
		print(xx)
		#while (math.cos(xx)) < 0.000001 and math.cos(xx) > 0:
			#xx += 0.01
		#	continue
	#	while math.cos(xx) > -0.0000001 and math.cos(xx) < 0:
			#xx -= 0.01
	#		continue
		xx = xx+ (math.cos(xx) * xx - math.sin(xx)) / (math.sin(xx) * xx)
		iterate += 1
	if xx - math.tan(xx) > 0.01:
		print("bad initial guess, try again")
	else:
		print("the solution:", xx, xx - math.tan(xx))
	
	
newton(5)
