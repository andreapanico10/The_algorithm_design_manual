'''Given string num representing a non-negative integer num, 
and an integer k, return the smallest possible integer 
after removing k digits from num.'''

class Solution:
    def removeKdigits(self, num: str, k: int, output_string: str) -> str:
        for i in range(10):
            position = 0
            for number in num:
                if(int(number) == i):
                    if ( len(num) - 1 - position >=  k - 1):
                        output_string += number  
                        k -= 1
                        num = num[:position] + num[position+1:]
                        if (k > 0):
                            return Solution().removeKdigits(num, k, output_string)  
                        else: 
                            output_string += num[position:]
                            if (output_string[0] == '0'):
                                output_string = output_string[1:]
                            return output_string
                    else:
                        break
                position +=1
        return '0'
    
        

solution = Solution()

outputs = ['','','','']
nums = ["1432219", "10200", "10", "10"]
Ks = [3, 1, 2, 1]

######                                            ######
# IMPORTANT LEARNING: how to iterate over multiple lists
######                                            ######

for (num, k, output) in zip(nums, Ks, outputs):
    output = solution.removeKdigits(num, k, output) 
    print('input: ', num, 'output: ',output)