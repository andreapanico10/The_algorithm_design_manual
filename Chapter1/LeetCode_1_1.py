class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        T = temperatures
        ans = [0]*len(T)
        for i in range(len(T)):
            for j in range(i+1, len(T)):
                if T[j] > T[i]:
                    ans[i] = j-i
                    break

        return(ans)
        