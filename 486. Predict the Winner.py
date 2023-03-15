class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def calc(nums,start,end):
            if start == end:
                return nums[start]
            else:
                return max(nums[start] -  calc(nums,start+1,end), nums[end] - calc(nums,start,end-1))
            
      
        if calc(nums,0,len(nums) -1) >= 0:
            return True
        else:
            return False
            
