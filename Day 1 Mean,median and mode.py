import numpy as np
from scipy import stats

def mean_func(X):
    print(np.mean(X))
    print(np.median(X))
    print(int(stats.mode(X)[0]))
    
N = int(input())
X = list(map(int, input().split()))

mean_func(X)