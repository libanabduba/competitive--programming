class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                temp = str(nums[i]) + str(nums[j])
                temp2 = str(nums[j]) + str(nums[i])
                if int(temp) > int(temp2):
                    continue
                else:
                    nums[i],nums[j] = nums[j], nums[i]
                    
        string = ""
        for i in range(len(nums)):
            if nums[0] == 0:
                return str(nums[0])
            string += str(nums[i])
        
        return string
                    
