# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(head):
            prev = None
            current = head
            while(current is not None):
                next = current.next
                current.next = prev
                prev = current
                current = next
            head = prev
            return head
        l1 = reverse(l1)
        l2 = reverse(l2)
    
        node = ListNode()
        curr = node
        temp = 0
        
        while l1 or l2 or temp:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            val = val1 + val2 + temp
            
            temp = val//10
            val = val%10
            
            curr.next = ListNode(val)
            curr = curr.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return reverse(node.next)
      