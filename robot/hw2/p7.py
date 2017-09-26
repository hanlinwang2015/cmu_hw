#! /usr/bin/python


import numpy as np

def getre():
    return np.array([[1.0, -12.0, 41.0, -42.0, 0], [0, 1, -12, 41, -42], [1, -2, -35, 0, 0], [0, 1, -2.0, -35.0, 0.0], [0, 0, 1.0, -2.0, -35]])

print(np.linalg.det(getre()))

def getnum():
	return (np.linalg.det(np.array([[-12.0, 41.0, -42.0, 0.0], [1, -12, 41, -42.0], [-2.0, -35.0, 0.0, 0.0], [1.0, -2.0, -35.0, 0]])) / np.linalg.det(np.array([[1, 41, -42, 0], [0, -12, 41, -42], [1, -35, 0, 0], [0, -2.0, -35, 0]])))
print(getnum())
