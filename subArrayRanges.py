class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
       
        total = 0
        for i in range(len(nums)):

            mini = nums[i]
            maxi = nums[i]
            for j in range(i,len(nums)):

                mini = min(mini,nums[j])
                maxi = max(maxi,nums[j])

                total += (maxi - mini)


        return total
