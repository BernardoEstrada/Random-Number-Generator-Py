import random as rnd
import numpy as np

def gen_triangular(N,a,b,c):
    numbers = []
    for _ in range(N):
        R = rnd.random()
        cut = (c - a)/(b - a)
        if 0 <= R <= cut:
            x = a + np.sqrt(R*(b - a)*(c - a))
        else:
            x = b - np.sqrt((1 - R)*(b - a)*(b - c))
        numbers.append(x)
    return numbers
    