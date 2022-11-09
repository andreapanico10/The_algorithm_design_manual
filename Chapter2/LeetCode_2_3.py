
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


My solution is correct, but is too slow
'''
from typing import List
import itertools
import numpy as np

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        for comb in itertools.combinations(nums, 4):
            if sum(comb) == target:
                output.append(list(sorted(comb)))

        # Solving the duplicates problem
        unique_output = np.unique(np.array(output), axis=0)

        return unique_output   

nums = [[1,0,-1,0,-2,2], [2,2,2,2,2], [-497,-480,-477,-470,-452,-448,-440,-412,-390,-381,-372,-372,-369,-366,-355,-346,-340,-337,-322,-321,-311,-296,-258,-249,-248,-232,-215,-199,-174,-154,-128,-122,-122,-117,-115,-113,-110,-89,-86,-84,-78,-71,-69,-53,-49,-35,-25,-21,-7,3,7,21,25,30,47,52,81,84,87,91,96,157,161,167,178,184,210,217,228,236,274,277,283,286,290,301,302,341,352,354,361,367,384,390,412,421,458,468,483,484,486,487,490,491]]               
targets = [0, 8, 8377]

solution = Solution()

for (num, target) in zip(nums, targets):
    output = solution.fourSum(num, target) 
    print('input: ', num, target, 'output: ',output)