class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
 
        # To store the answer
        list = [0] * n
        stack = []

        # Traverse all the temperatures
        for i in range(n):

            # Check if current index is the
            # next warmer temperature of
            # any previous indexes
            while(len(stack) != 0 and temperatures[stack[-1]] < temperatures[i]):
                list[stack[-1]] = i - stack[-1]

                # Pop the element
                stack.pop(-1)

            # Push the current index
            stack.append(i)
        return list
