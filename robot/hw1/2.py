#! /usr/bin/python
import scipy as sp
import scipy.linalg as spl
import numpy as np
LA = np.linalg
b = np.array([[4, 7, 0],[2, 2, -6], [1, 2, 1]])
c = np.array([[4, 8, 0, 0], [2, 0, -2, 0], [0, 4, -1, 0], [0, -2, 0, 2], [0, 0, 2, -1]])
d = np.array([[2, 2, 5], [3, 2, 5], [1, 1, 5]])
u1, s1, vh1 = LA.svd(b, full_matrices=False)
u2, s2, vh2 = LA.svd(c, full_matrices=False)
u3, s3,vh3 = LA.svd(d, full_matrices=False)

print("\nSVD for matrix A:\n")
print("U =")
print(u1)
print("S=")
print(s1)
print("V =")
print(vh1)

print("\nSVD for matrix B:\n")
print("U =")
print(u2)
print("S=")
print(s2)
print("V =")
print(vh2)

print("\nSVD for matrix C:\n")
print("U =")
print(u3)
print("S=")
print(s3)
print("V =")
print(vh3)


b = sp.array([[4, 7, 0],[2, 2, -6], [1, 2, 1]])
c = sp.array([[4, 8, 0, 0], [2, 0, -2, 0], [0, 4, -1, 0], [0, -2, 0, 2], [0, 0, 2, -1]])
d = sp.array([[2, 2, 5], [3, 2, 5], [1, 1, 5]])
u1, s1, vh1 = spl.lu(b)
u2, s2, vh2 = spl.lu(c)
u3, s3,vh3 = spl.lu(d)

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
print("V =")
print(vh3)


