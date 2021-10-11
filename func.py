import random as rnd

def gen_func(N):
    numbers = []
    for _ in range(N):
        R = rnd.random()
        numbers.append(3 ** R / 2)
    return numbers
    