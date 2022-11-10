#!/bin/python3
'''
Find the number of ways that a given integer, X , can be expressed as the sum of the  N^th
powers of unique, natural numbers.
For example, if X=13 and N=2, we have to find all combinations of unique squares adding up to 13.
 The only solution is 2^2 + 3^2.
Function Description
Complete the powerSum function in the editor below. It should return an integer that represents the number of possible combinations.
powerSum has the following parameter(s):
X: the integer to sum to
N: the integer power to raise numbers to
Input Format
The first line contains an integer X. 
The second line contains an integer N.

'''
import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#

def powerSum(X, N):
    # Write your code here

    output = []
    nums = [x for x in range(1,math.ceil(X**(1/N)+1))]

    for combinations in range(1,len(nums)+1):
        for comb in itertools.combinations(nums, combinations):
            if(sum([x**N for x in list(comb)])) == X:
                output.append(list(comb))

    return len(output ) 
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
