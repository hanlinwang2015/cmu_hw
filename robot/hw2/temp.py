#! /usr/bin/python

temp = 10000 * [1.0]
import math
def gen1():
        xx = []
	yy = []
	for i in range(0, 7):
		xx.append(1.0 + i * 0.5)
		yy.append(math.pow(math.log(xx[i], 7), 2))
	return xx, yy		
def gen2(n):
	xx = []
	yy = []
	for i in range(0, n):
		xx.append(i * 2.0 / n - 1)
		yy.append(5.0 / (1 + 36 * xx[i] * xx[i]))
	return xx, yy
#def gen3():
#xx = [1, 2, 3]
#yy = [1, 4, 9]
def F(start, end, xx, yy):
	if end > 20:
		print(end)	
	if start == end:
		return yy[start]
	else:
		return (F(start, end - 1, xx, yy) - F(start + 1, end, xx, yy)) / (xx[start] - xx[end])
def getP(xx, yy):
	result = []
	for i in range(0, len(xx)):
		result.append(F(0, i, xx, yy))
	return result
	
def getvalue(xx, yy, ff, tar, n):
	if n == len(xx) - 1:
		return ff[n]
	else:
		return getvalue(xx, yy, ff, tar, n + 1) * (tar - xx[n]) + ff[n]
def p1():
	xx, yy = gen1()
	print("The answer for a is",  getvalue(xx, yy, getP(xx, yy), 2.25, 0))
p1()
def test():
	xx = [1.0, 2.0, 3.0, 4.0]
	yy = [4.0, 5.0, 6.0, 7.0]
	print("the answer for test is", getP(xx, yy), getvalue(xx, yy, getP(xx, yy), 9.0, 0))
test()
def p2():
	xx, yy = gen2(2)	
	print("the answer for b.1 is", getP(xx, yy), getvalue(xx, yy, getP(xx, yy), 0.05, 0))
	xx, yy = gen2(4)
	print("the anmswe for b.2 is", getvalue(xx, yy, getP(xx, yy), 0.05, 0))
	xx, yy = gen2(40)
	print("the answer for b.3 is", getvalue(xx, yy, getP(xx, yy), 0.05, 0))
p2()
