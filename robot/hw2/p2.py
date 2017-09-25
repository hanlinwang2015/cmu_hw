#! /usr/bin/python

temp = 1440 * [0.0]
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
	for i in range(0, n + 1):
		xx.append(i * 2.0 / n - 1)
		yy.append(5.0 / (1 + 36 * xx[i] * xx[i]))
	return xx, yy
#def gen3():
#xx = [1, 2, 3]
#yy = [1, 4, 9]
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
def p3():
	max_ = 0.0
	max_x = 0.0
	nn = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 40]
	for j in nn:
		xx, yy = gen2(j)
		re = getP(xx, yy)
		max_ = 0.0
		for i in range(1,3000):
			fake = -1.0 + i * 2.0 /3000
			er = 5.0 / (1 + 36 * fake * fake) - getvalue(xx, yy, re, fake, 0)
			if abs(er) > max_:
				max_ = abs(er)
				max_x = fake
		print("the max for n = ", j, max_, max_x)
p3()

		
