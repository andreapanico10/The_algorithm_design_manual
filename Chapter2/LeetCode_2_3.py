
'''
Given an array nums of n integers, return an array of all the unique quadruplets
 [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Ex 1
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Ex 2
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

'''
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        return None

solution = Solution()

nums = [[1,0,-1,0,-2,2],[2,2,2,2,2] ]
targets = [0,8]

for (num, target) in zip(nums, targets):
    output = solution.fourSum(num) 
    print('input: ', num, target, 'output: ',output)