class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
       
        heap = []
        for i in matrix:
            for j in i:
                heappush(heap,j)
        
        for i in range(k):
            result = heappop(heap)

        return result
            
