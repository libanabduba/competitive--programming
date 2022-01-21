class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head
        if head == None:
            return None
        while head.next!=None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
            
        return temp
