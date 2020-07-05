import numpy as np

def randn(lo,hi):
    # fline = open("seed.txt").readline().rstrip()
    # ranseed = int(fline)
    # np.random.seed(ranseed)
    return np.random.rand()*(hi-lo) + lo
    return np.random.randn()*(((hi-lo)/2)/3) + (hi+lo)/2 
    # for reference https://stackoverflow.com/questions/2751938/random-number-within-a-range-based-on-a-normal-distribution

def randni(lo,hi):
    # fline = open("seed.txt").readline().rstrip()
    # ranseed = int(fline)
    # np.random.seed(ranseed)
    return int(np.random.randn()*(((hi-lo)/2)/3) + (hi+lo)/2 )
    # for reference https://stackoverflow.com/questions/2751938/random-number-within-a-range-based-on-a-normal-distribution