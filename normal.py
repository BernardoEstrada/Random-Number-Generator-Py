import numpy as np

def gen_normal(N, miu, sigma):
    U1 = np.random.rand(N)
    U2 = np.random.rand(N)
    x = miu + sigma * np.sqrt(-2 * np.log(U1)) * np.cos(2 * np.pi * U2)
    return x
    