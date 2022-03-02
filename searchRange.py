class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        if len(nums) == 0:
            return [-1,-1]
        if (len(nums)) == 1:
	        return [-1, -1] if nums[0] != target else [0, 0]
        
        while left <= right:
            mid = left + (right-left)//2
            
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                while nums[left] != target:
                    left += 1
                while nums[right] != target:
                    right -= 1
                return [left, right]

        return [-1, -1]
                
