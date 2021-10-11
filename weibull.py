import numpy as np
import random as rnd

def gen_weibull(N, alpha, beta):
    numbers = []
    for _ in range(N):
        R = rnd.random()
        x = alpha * (-np.log(R))**(1/beta)
        numbers.append(x)
    return numbers
