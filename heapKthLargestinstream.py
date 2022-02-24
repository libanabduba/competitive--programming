class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapify(self.nums)
    def add(self, val: int) -> int:
        heappush(self.nums,val)
        while len(self.nums) > self.k:
            heappop(self.nums)

        return self.nums[0]
  
