'''Given an integer n, return an array ans of length n + 1 
such that for each i (0 <= i <= n), ans[i] is the number of 1's in the 
binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

'''
from typing import List

class Solution:

    # the solution lies behind the restless fraction of a number over 2
    # the number of recursive division by 2 with residual is equal
    # to the number of 1 in the binary representation

    ''' Okay, I found this solution in 5 minutes, but is only faster than 5% of the other
    code, come back to solve it again, better!'''

    def transformDecimalInBinary(self, n: int) -> int:
        
        count = 0        
        residual = n
        
        while residual > 0:
            result = residual / 2
            
            if(result != int(result)):
                count += 1

            residual = int(result)
    
        return count


    def countBits(self, n: int) -> List[int]:
        
        ans = [0]*(n+1)

        for i in range(n+1):
            ans[i] = self.transformDecimalInBinary(i)

        return ans


solution = Solution()

n = [2,5]

for num in n:
    output = solution.countBits(num) 
    print('input: ', num, 'output: ',output)