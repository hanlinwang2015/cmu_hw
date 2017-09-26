#! /usr/bin/python

import csv
import numpy as np

import math
filename = "Image Data.txt"
data = []
for i in range(0, 98):
	reader = csv.reader(open('/home/hanlin/cmu_hw/robot/hw2/paths.txt'),delimiter=" ")
	col = list(zip(*zip(*reader)))[i] 
	data.append(col)
#	print(i)
temp = 1440 * [0.0]
print(float(data[0][0]) - 1)
def convex(x1, y1, x2, y2, x3, y3, x, y):
	vx0 = x1
	vy0 = y1
	vx1 = x2 - x1
	vy1 = y2 - y1
	vx2 = x3 - x1
	vy2 = y3 - y1
	kk = vx1 * vy2 - vy1 * vx2
	dist = ((x - x1)**2 + (y - y1)**2)**0.5 + ((x - x2)**2 + (y - y2)**2)**0.5 + ((x-x3)**2 + (y - y3)**2)**0.5
#	print(kk)
	if abs(kk) > 0.000000001:

		a = (x *  vy2 - y * vx2 - vx0 * vy2 + vy0 * vx2) / kk
		b = (x * vy1 - y * vx1 - vx0 * vy2 + vy0 * vx2) / kk
		if a >= 0 and b >= 0 and a + b < 1:
			return 1, a, b, dist
		else:
			return 0, a, b, dist
	else:
		if abs(x *  vy2 - y * vx2 - vx0 * vy2 + vy0 * vx2) < 0.00000001:
			return 1, -1, -1, dist
		else:
			return 0, -1, -1, dist
	#print(convex(0.0, 0.0, 1.0, 0.0, 1/2.0, 1/2.0, 3.0, 1.0))
def weight(x, y):
	mina = -1.0
	for i in range(0, 49):
		for j in range(i, 49):
			for k in range(j,49):
				if i != j and j != k:
#					print(i, j, k)
					det = convex(float(data[2 * i][0]), float(data[2 * i + 1][0]),float(data[2 * j][0]), float(data[2 * j + 1][0]), float(data[2 * k][0]), float(data[2 * k + 1][0]), x, y)
		
					if det[0]  == 1:
						maxdist = 0
						for m in range (1, 50):
							if (abs(float(data[2 * i + 1][m]) - float(data[2 * j + 1][m])) > 3 and abs(float(data[2 * i][m])) > 3.5 and abs(float(data[2 * i][m])) < 6.5) or (abs(float(data[2 * k + 1][m]) - float(data[2 * j + 1][m])) > 3 and abs(float(data[2 * k][m])) > 3.5 and abs(float(data[2 * k][m])) < 6.5):
								continue
							else:	
								if mina > det[3] or mina < 0:
									mina = det[3]
									cadidate = [i, j, k]
									fdet = det
	return cadidate, fdet
print(weight(0.8, 1.8))
