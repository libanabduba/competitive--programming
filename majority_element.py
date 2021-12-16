class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1
        list = []
        for i in dic:
            if dic[i] > len(nums)/3:
                list.append(i)
                
        return list
