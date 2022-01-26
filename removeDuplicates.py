class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0
        right = 1
        while right < len(nums):
            if nums[left] == nums[right]:
                nums.pop(left)
            else:
                left += 1
                right += 1
                
                
        return len(nums)
                
        
