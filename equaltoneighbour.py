class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        leftindex,rightindex = 0, len(nums) - 1
        
        values = []
        
        while len(nums) != len(values):
            
            values.append(nums[leftindex])
            leftindex+=1
            
            if leftindex <= rightindex:
                values.append(nums[rightindex])
                rightindex-=1
        return values
