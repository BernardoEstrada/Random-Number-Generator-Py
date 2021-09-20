# import numpy as np
import pandas as pd
import math

def chi_squared(
        file,
        h0,
        buckets=None,
        width=None,
        min=None,
        max=None,
        decimals = 4
    ):
    data = pd.read_csv(file, delimiter="\n", header=None)
    data = data.round(decimals)
    N = len(data[0].index)

    dMin = math.ceil(data[0].min())     if min is None else min
    dMax = math.floor(data[0].max())    if max is None else max

    c = int(round(1 + 3.33 * math.log(N, 10))) \
        if buckets is None else buckets
    w = round(((dMax - dMin) / c + pow(10, -decimals)), decimals) \
        if width is None else width

    expected = N / c

    classes = pd.DataFrame(
        columns=[
            'interval',
            'observed',
            'expected',
            '(O-E)^2/E'
            ]
        )

    for i in range(c):
        lower = (dMin + (w * i))
        upper = dMin + w * (i + 1)

        classes.at[i, 'interval'] = \
            '(' + \
            str(round(lower, decimals)) + \
            ' - ' + \
            str(round(upper, decimals)) + \
            ']'

        obs = data[(data[0] >= lower) & (data[0] < upper)].shape[0]
        classes.at[i, 'observed'] = obs
        classes.at[i, 'expected'] = expected
        classes.at[i, '(O-E)^2/E'] = round(
            (obs - expected) ** 2 / expected,
            decimals
        )

    x2 = round(classes['(O-E)^2/E'].sum(), decimals)
    return (classes, x2, x2<h0)


if __name__ == "__main__":
    ## chi_squared(filename, buckets, width, min, max)
    h0 = 16.9190
    (table, x2, h0R) = chi_squared("chi_data.txt", h0, 10, 0.1, 0, 1)
    
    print()
    print(table)

    print()
    print('X^2 = ' + str(x2))

    print()
    print(
        'H0 is ' +
        ('not rejected' if h0R else 'rejected') +
        ' since ' +
        (
            str(x2) +
            (' <= ' if h0R else ' > ') +
            str(h0)
        )
    )

    print()
