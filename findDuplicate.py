class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic = {}
        arr = []
        for i in range(1,max(nums) + 1):
            dic[i] = 0
            arr.append(i)
        for number in nums:
            left = 0
            right = len(arr) - 1
            
            while left <= right:
                mid = left + (right - left)//2
                
                if arr[mid] > number:
                    right = mid - 1
                elif arr[mid] < number:
                    left = mid + 1
                else:
                    dic[number] += 1
                    break
                    
        for i in dic:
            if dic[i] > 1:
                return i
                    
