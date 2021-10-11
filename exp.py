import random as rnd
import numpy as np

def gen_exp(N, lam):
    numbers = []
    for _ in range(N):
        R = rnd.random()
        x = np.log(R)/lam
        numbers.append(x)
    return numbers
    
if __name__ == '__main__':
    # N = int(input("N = "))
    # lam = float(input("lambda = "))
    N = 10000
    lam = 100
    numbers = gen_exp(N, lam)
    np.savetxt('out.txt', numbers)
