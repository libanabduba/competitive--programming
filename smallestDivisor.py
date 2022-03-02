class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        
        while left <= right:
            mid = left + (right - left) // 2
            divSum = self.divisorSum(nums, mid)
            if divSum > threshold:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1
        
        return ans
            
    def divisorSum(self, nums, divisor):
        return sum(ceil(num / divisor) for num in nums)
