class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_stones = [-1 * i for i in stones]
        heapify(new_stones)
        while len(new_stones) > 1:
            max1 = -1 * heappop(new_stones)
            max2 = -1 * heappop(new_stones)
            if max1 != max2:
                temp = max1 - max2
                heappush(new_stones,-1*temp)
        print(new_stones)
        if len(new_stones) == 0:
            return 0
        return -1 * new_stones[0]
                
        
