'''Given string num representing a non-negative integer num, 
and an integer k, return the smallest possible integer 
after removing k digits from num.'''

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        partial_string = ""
        selected = 0

        i = 0
        while i < 10:
            position = 0
            for number in num:
                if(int(number) == i):
                    if ( len(num) - 1 - position >=  len(num)-k - selected ):
                        partial_string += number  
                        selected += 1
                        i = 0
                    else:
                        break
                position +=1
            i += 1
        print(partial_string)