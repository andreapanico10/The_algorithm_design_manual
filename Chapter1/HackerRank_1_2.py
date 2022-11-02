#!/bin/python3

import os
#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    pos1 = x1
    pos2 = x2
 
    if x2 < x1:
        pos1 = x2
        pos2 = x1
        v1, v2 = v2, v1
    
    if (v1 <= v2):
        return 'NO' 
   
    while(pos1 <= pos2):
        
        if (pos1 == pos2):
            return 'YES'
        
        pos1 = pos1 + v1
        pos2 = pos2 + v2
        
    return 'NO'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
