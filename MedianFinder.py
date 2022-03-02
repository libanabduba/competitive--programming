class MedianFinder:

    def __init__(self):
        self.leftheap = []
        self.rightheap = []
    
    def addNum(self, num: int) -> None:
        heappush(self.leftheap,-1 * num)
        
        if self.leftheap and self.rightheap and  -1 * self.leftheap[0] > self.rightheap[0]:
            val = heappop(self.leftheap)
            heappush(self.rightheap, -1 * val)
            
        if len(self.leftheap) > len(self.rightheap) + 1:
            val = heappop(self.leftheap)
            heappush(self.rightheap, -1 * val)
        if len(self.leftheap)+ 1 < len(self.rightheap):
            val = heappop(self.rightheap)
            heappush(self.leftheap, -1 * val)
            


    def findMedian(self) -> float:
        if len(self.leftheap) > len(self.rightheap):
            return -1 * self.leftheap[0]
        elif len(self.leftheap) < len(self.rightheap):
            return self.rightheap[0]
        else:
            return (-1 * self.leftheap[0] + self.rightheap[0])/2
