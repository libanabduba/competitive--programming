# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        temp = head
        
        if head == None:
            return None
        while head != None:
            arr.append(head)
            head = head.next
            
        def myFunc(temp):
            return temp.val
            
        arr.sort(key=myFunc)
#         print(arr)
        
        for i in range(len(arr)):
            if i == len(arr) -1:
                arr[i].next = None
                break
            arr[i].next = arr[i+1]
       
        head = arr[0]
        
        
        return head
        
                

        
        
