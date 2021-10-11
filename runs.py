
import pandas as pd
import numpy as np

def runsGeneratedSigns(arr):
    res = []
    for i in range(arr.shape[0] - 1):
        res.append(arr.at[i + 1, 0] > arr.at[i, 0])
    return res

def printRunsSigns(arr):
    for i in range(len(arr)):
        print('+' if arr[i] else '-', end=' ')
    print()
    print("(+): " + str(arr.count(True)), end=', ')
    print("(-): " + str(arr.count(False)), end=', ')
    print("Total: " + str(len(arr)))


def getRuns(arr):
    run = arr[0]
    posRuns = 1 if run else 0
    negRuns = 0 if run else 1
    for i in range(len(arr)):
        if arr[i] != run:
            run = arr[i]
            posRuns += 1 if run else 0
            negRuns += 0 if run else 1
    return posRuns, negRuns


def runs_data(data, h0, decimals = 4):
    signs = runsGeneratedSigns(data)
    runs = getRuns(signs)

    miu  = round((2 * len(signs) - 1) / 3, decimals)
    sigma = round(np.sqrt((16 * len(signs) - 29) / 90), decimals)
    Zscore = round((sum(runs) - miu) / sigma, decimals)

    h0R = abs(Zscore) < h0
    
    res = {
        "signs": signs,
        "runs": runs,
        "miu": miu,
        "sigma": sigma,
        "Zscore": Zscore,
        "h0R": h0R
    }

    return res


def runs_file(fname, h0, decimals=4):
    data = pd.read_csv(fname, delimiter="\n", header=None)
    return runs_data(data, h0, decimals)

if __name__ == '__main__':
    h0 = 1.96
    runsRes = runs_file('out.txt', h0, 4)

    # printRunsSigns(runsRes['signs'])
    print("Positive runs: " + str(runsRes['runs'][0]))
    print("Negative runs: " + str(runsRes['runs'][1]))
    print("Miu: " + str(runsRes['miu']))
    print("Sigma: " + str(runsRes['sigma']))
    print("Z-score: " + str(runsRes['Zscore']))
    print()
    print(
        'H0 is ' +
        ('not rejected' if runsRes['h0R'] else 'rejected') +
        ' since ' +
        (
            '|' + str(runsRes['Zscore']) + '|' +
            (' <= ' if runsRes['h0R'] else ' > ') +
            '|' + str(h0) + '|'
        )
    )
    print()
