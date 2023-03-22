class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        right = 0

        add = nums[0]
        ans = len(nums)
        if sum(nums) < target:
            return 0

        while right < len(nums):
            if add >= target:
                window_size = right - left + 1
                ans = min(ans, window_size )
                add -= nums[left]
                left += 1

            else:
                right += 1
                if right < len(nums):
                    add += nums[right]

        return ans
