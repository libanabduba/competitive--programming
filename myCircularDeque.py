 from collections import deque
 class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = deque([])
        self.size = k

    def insertFront(self, value: int) -> bool:
        if len(self.queue) < self.size:
            self.queue.appendleft(value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.queue) < self.size:
            self.queue.append(value)
            return True
        return False
            

    def deleteFront(self) -> bool:
         if len(self.queue) != 0:
            self.queue.popleft()
            return True
         return False

    def deleteLast(self) -> bool:
         if len(self.queue) != 0:
            self.queue.pop()
            return True
         return False

    def getFront(self) -> int:
        if len(self.queue) != 0:
            return self.queue[0]
        return -1

    def getRear(self) -> int:
        if len(self.queue) != 0:
            return self.queue[-1]
        return -1

    def isEmpty(self) -> bool:
         if len(self.queue) != 0:
            return False
         return True

    def isFull(self) -> bool:
         if len(self.queue) == self.size:
            return True
         return False
