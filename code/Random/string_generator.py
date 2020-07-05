import string
import random

def rands(strlen):
    # fline = open("seed.txt").readline().rstrip()
    # ranseed = int(fline)
    # random.seed(ranseed)
    return''.join([random.choice(string.ascii_lowercase) for i in range(strlen)])
