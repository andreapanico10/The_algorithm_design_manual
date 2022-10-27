'''Write a function to perform integer division without
 using either the / or * operators. Find a fast way to do it.'''

from audioop import mul
import numpy as np

# input parameters
a = 103
b = 7

def integer_division(a,b):
    
    # subtract from accumulator
    accumulator = a
    multiple_counter = 0
    change = 0

    while (accumulator >= 0):
        
        accumulator -= b
        if(accumulator >= 0):
            multiple_counter += 1
        else:
            change += accumulator + b

    return multiple_counter, change

result, change = integer_division(a,b)

print('{}/{} = {} with change = {}'.format(a,b,result, change))
