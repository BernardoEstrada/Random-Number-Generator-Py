import numpy as np

def gen_LCG(N, x0, a, c, m):
    R = np.empty(N)
    for i in range(N):
        x_next = (a*x0 + c) % m
        R[i] = x_next / m
        x0 = x_next
    return R

if __name__ == '__main__':
    N = 10
    x0 = 6
    a = 32
    c = 3
    m = 80
    R = gen_LCG(N, x0, a, c, m)
    print(R)
