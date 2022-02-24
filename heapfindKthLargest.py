class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr =[-i for i in nums]
        heapify(arr)
        for i in range(k):
            result = heappop(arr)
            
        return -1 * result
