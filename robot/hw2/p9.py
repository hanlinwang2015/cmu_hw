#! /usr/bin/python

import csv
import numpy as np

import math
filename = "Image Data.txt"
data = []
for i in range(0, 50):
	reader = csv.reader(open('/home/hanlin/cmu_hw/robot/hw2/paths.txt'),delimiter=" ")
	col = list(zip(*zip(*reader)))[i] 
	data.append(col)
	print(col)
temp = 1440 * [0.0]
def F(n, xx, yy):
	if n == 1: 
		temp[n] = yy[0]
	else:
		num = (n - 1) * n / 2
		for i in range(num + 1, num + n + 1):
			if i == (num + 1):
				temp[i] = yy[n - 1]
#				print(yy[n - 1])
			else:
				temp[i] =  (temp[i - 1] - temp[i - n]) / (xx[n - 1] - xx[n - i + num])
	
def getP(xx, yy):
	result = []
	for i in range(1, len(xx) + 1):
		F(i, xx, yy)
		result.append(temp[(i + 1) * i / 2])
#	print(temp[1:100])
	return result
	
def getvalue(xx, yy, ff, tar, n):
	if n == len(xx) - 1:
		return ff[n]
	else:
		return getvalue(xx, yy, ff, tar, n + 1) * (tar - xx[n]) + ff[n]

