# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        list = []
        while head != None:
            list.append(head.val)
            head = head.next
            
        arr = list[::-1]
        print(arr)
        print(list)
        
        for i in range(len(list)):
            if arr[i] != list[i]:
                return False
        
        return True
            
