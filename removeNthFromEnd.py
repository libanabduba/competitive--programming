class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        value = head
        temp = head
        count = 0
      
        while head != None:
            count += 1
            head = head .next
        index = 0 
        
        if count == 1:
            return head
        if count == n:
            return value.next
        
        while temp != None:
            index += 1
            if index == count - n:
                temp.next = temp.next.next
                break
            temp = temp.next
            
        return value
