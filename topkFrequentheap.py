import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        print(dic)
        freq = [(-1 * values,key) for key,values in dic.items()]
        heapq.heapify(freq)
        result = []
        print(freq)
        
        for i in range(k):
            temp = heapq.heappop(freq)
            result.append(temp[1])
       
        return result
        
