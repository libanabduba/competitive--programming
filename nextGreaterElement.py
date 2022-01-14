class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        monstack = [nums2[0]]
        arr = []
        for i in range(1,len(nums2)):
            if nums2[i] > monstack[-1]:
                dic[monstack[-1]] = nums2[i]
                monstack.pop(-1)
                monstack.append(nums2[i])
                while len(monstack) > 1 and monstack[-1] > monstack[-2]:
                    dic[monstack[-2]] = monstack[-1]
                    monstack.pop(-2)
                  
                        
                
            else:
                monstack.append(nums2[i])
        
        if len(monstack) != 0:
            for i in monstack:
                dic[i] = -1
                
                
        for i in nums1:
            arr.append(dic[i])
            
        return arr
            
        
