class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(1,len(heights)):
            diff = heights[i] - heights[i -1]
            if diff > 0:
                if len(heap) < ladders:
                    heappush(heap,diff)
                else:
                    br = diff
                    if len(heap) > 0 and heap[0] < diff:
                        br = heappop(heap)
                        heappush(heap,diff)
                    
                    if bricks - br >= 0:
                        bricks -= br
                    else:
                        print(i)
                        return i - 1
        return len(heights) - 1
                
