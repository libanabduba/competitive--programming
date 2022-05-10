class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        

class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        temphead = self.head
        for _ in range(index+1):
            temphead = temphead.next
            
        return temphead.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
         self.addAtIndex(self.size,val)

    def addAtIndex(self, index: int, val: int) -> None:
        
        
        if index > self.size:
            return 
        
        self.size += 1
        
        temphead = self.head
        
        for _ in range(index):
            temphead = temphead.next
        to_add = Node(val)    
        to_add.next = temphead.next
        temphead.next = to_add
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        temphead = self.head
        
        for _ in range(index):
            temphead = temphead.next
            
            
        temphead.next = temphead.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
