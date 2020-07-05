import numpy as np

def rand(lo,hi):
    # fline = open("seed.txt").readline().rstrip()
    # ranseed = int(fline)
    # np.random.seed(ranseed)
    return np.random.rand()*(hi-lo) + lo
