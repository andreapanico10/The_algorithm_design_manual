class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        support_array = []
        counter = 0
        for i in range(len(temperatures)):
            if(i == 0):
                support_array.append(0)
            else:
                support_array.append(counter + (temperatures[i] - temperatures[i-1]))
                counter = support_array[i]

        output = []
        for i in range(len(support_array)):
            counter = 0
            if(i == len(support_array)-1):
                output.append(counter)

            for j in range (i+1, len(support_array)):
                counter +=1

                if(support_array[j] > support_array[i]):
                    output.append(counter)
                    counter = 0
                    break
        temperatures_len = len(temperatures)
        output_len = len(output)
        for i in range(temperatures_len - output_len):
            output.append(0)
            
        return(output)