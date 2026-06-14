#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Sum of digits of n, multiplied by k (since p = n repeated k times)
    digit_sum = sum(int(d) for d in n) * k
    return reduce_to_single_digit(digit_sum)

def reduce_to_single_digit(num):
    # Base case: already a single digit
    if num < 10:
        return num
    
    # Sum the digits and recurse
    digit_sum = sum(int(d) for d in str(num))
    return reduce_to_single_digit(digit_sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
