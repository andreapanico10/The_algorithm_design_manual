#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/array-left-rotation/problem

# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

### my code ###
def rotateLeft(d, arr):
    
    if arr == None:
        return None
    
    for i in range (d % len(arr)):
        head = arr.pop(0)
        arr.append(head)
    return arr
### end of my code ###

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])
    
    arr = list(map(int, input().rstrip().split()))
    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
