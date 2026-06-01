#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
arr = []
def miniMaxSum(arr):
    minsum = 0
    maxsum = 0
    total = 0
    for i in arr:
        total = i+total
    min1 = min(arr)
    max1 = max(arr)
    print(total-max1,total-min1 )
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)