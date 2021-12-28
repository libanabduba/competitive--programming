class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i  in nums:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1
        list = []
        for i in dic:
            list.append([dic[i],i])
        arr = sorted(list,reverse = True)
        
        arr1 = []
        for i in range(k):
            arr1.append(arr[i][1])
        
        return arr1
            
