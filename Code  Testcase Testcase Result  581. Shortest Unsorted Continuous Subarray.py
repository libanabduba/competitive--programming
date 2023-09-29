class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        Max =  float('-inf')
        Min =  float('inf')

        n = len(nums)

        if n == 1: return 0


        for i in range(n):

            if i == 0: 
                if nums[i] > nums[i + 1]:
                    Max = max(nums[i], Max)
                    Min = min(nums[i], Min)
                   

            elif i == n - 1:
                if nums[i] < nums[i - 1]:
                    Max = max(nums[i], Max)
                    Min = min(nums[i], Min)

            else: 
                if nums[i] < nums[i - 1] or nums[i + 1] < nums[i]:
                    Max = max(nums[i], Max)
                    Min = min(nums[i], Min)


        if Max == float('-inf') or Min == float('inf'):
            return 0
        
        i = 0
        j = n - 1

        while i < n and nums[i] <= Min:
            i += 1

        while j >= 0 and nums[j] >= Max:
            j -= 1

        return (j - i + 1)



        


     



            

            



