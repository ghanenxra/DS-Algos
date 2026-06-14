#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#

def powerSum(X, N):
    return compute(X, N, 1)

def compute(X, N, start):
    num_pow = pow(start, N)
    
    if X == 0:
        return 1
    
    if X < 0 or num_pow > X:
        return 0
        
    return compute(X - num_pow, N, start + 1) + compute(X, N, start + 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()