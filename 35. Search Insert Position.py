class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        mid = 0
        if target < nums[0]:
            return 0

        while left <= right:
            mid = left + (right - left)//2

            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid

        if nums[right] > target:
            return right - 1
        return right + 1
