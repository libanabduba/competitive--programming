# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        left = head
        if left == None:
            return None
        right = head.next if head != None else None
        arr = []
        if left.next == None:
            return left
        while right != None:
            
            node1 = ListNode(left.val)
            node2 = ListNode(right.val)
            
            arr.append(node2)
            arr.append(node1)
            
            left = left.next.next if left.next != None else None
            right = right.next.next if right.next != None else None
        if left != None and left.next == None:
            arr.append(ListNode(left.val))   
        for i in range(len(arr)):
            if i == len(arr) -1:
                arr[i].next = None
                break
            arr[i].next = arr[i+1]
         
        return arr[0]
