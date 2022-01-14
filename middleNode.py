class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        arr = []
        
        while head != None:
            arr.append(head)
            head = head.next
            
        return arr[len(arr)//2]
