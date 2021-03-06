#! /usr/bin/python
import scipy as sp
import scipy.linalg as spl
import numpy as np

b = sp.array([[2, 1, 3],[2, 1, 2], [5, 5, 5]])
c = sp.array([[4, 7, 0], [2, 2, -6], [1, 2, 1]])
d = sp.array([[4, 7, 0], [2, 2, -6], [1, 2, 1]])
u1, s1, vh1 = spl.lu(b)
u2, s2, vh2 = spl.lu(c)
u3, s3,vh3 = spl.lu(d)
e = sp.array([[3], [5], [1]])
f = sp.array([[[18], [-12], [8]]])

ee = spl.pinv(c).dot(e)
ff = spl.pinv(c).dot(f)
print("\nLU for matrix A:\n")
print("P =")
print(u1)
print("S=")
print(s1)
print("V =")
print(vh1)
print(ee)
print(ff)
print("\nLU  for matrix B:\n")
print("p =")
print(u2)
print("S=")
print(s2)
print("V =")
print(vh2)

print("\nLU  for matrix C:\n")
print("P =")
print(u3)
print("S=")
print(s3)
print("V=")
print(vh3)

u1, s1, vh1 = spl.svd(b)
u2, s2, vh2 = spl.svd(c)
u3, s3,vh3 = spl.svd(d)

print("\nLU for matrix A:\n")
print("P =")
print(u1)
print("S=")
print(s1)
print("V =")
print(vh1)

print("\nLU  for matrix B:\n")
print("p =")
print(u2)
print("S=")
print(s2)
print("V =")
print(vh2)

print("\nLU  for matrix C:\n")
print("P =")
print(u3)
print("S=")
print(s3)
print("V=")
print(vh3)


