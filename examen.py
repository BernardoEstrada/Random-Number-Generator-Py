import numpy as np
import random as rnd

def examen(N,a,b,c):
    numbers = []
    for _ in range(N):
        R = rnd.random()
        if 0 <= R < a:
            x = 2 * np.sqrt(R*10/3) - 2
        elif a <= R < b:
            x = (R - 0.3) / 0.3
        elif b <= R < c:
            x = 3 - (4 / 3 * np.sqrt(5 - 5*R))

        numbers.append(x)
    return numbers