import numpy as np
import math 

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        nums.sort()
        n=len(nums)
        k = (n+1) // 2
        ar1=nums[:k]
        ar2=nums[k:]
        ar2.reverse()
        ar1.reverse()
        i1=0
        i2=0
        for i in range(n):
            if(i%2==0):
                nums[i]=ar1[i1]
                i1+=1
            else:
                nums[i]=ar2[i2]
                i2+=1
                
    
        