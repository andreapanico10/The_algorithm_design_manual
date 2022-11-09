#!/bin/python3
'''
A pangram is a string that contains every letter of the alphabet. 
Given a sentence determine whether it is a pangram in the English alphabet.
Ignore case. Return either pangram or not pangram as appropriate.
Example 

The string contains all letters in the English alphabet, so return pangram.
'''
import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    s = s.lower() # Lower case
    s = s.replace(" ","") # Suppress blanks
    s = ''.join(sorted(list(set(s)))) #order the string
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    if s == alphabet:
        return 'pangram'
    else:
        return 'not pangram'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s.lower())

    fptr.write(result + '\n')

    fptr.close()
