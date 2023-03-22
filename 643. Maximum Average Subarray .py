class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k

        add = sum(nums[left:right])
        avg = add/k
        maxi = avg

        while right < len(nums):
            add += nums[right]
            add -= nums[left]
            left += 1
            avg = add/k
            if avg > maxi:
                maxi = avg

            right += 1

        return maxi
