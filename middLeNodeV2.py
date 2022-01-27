# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        right = head
        left = head
        
        while right != None and right.next != None:
            right = right.next.next
            left = left.next
            
        return left
            
