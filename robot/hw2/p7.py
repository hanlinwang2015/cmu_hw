#! /usr/bin/python


import numpy as np

def getre():
    return np.array([[1.0, -12.0, 41.0, -42.0, 0], [0, 1, -12, 41, -42], [1, -2, -35, 0, 0], [0, 1, -2.0, -35.0, 0.0], [0, 0, 1.0, -2.0, -35]])

print(np.linalg.det(getre()))
