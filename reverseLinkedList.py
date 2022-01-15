class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        
        while head != None:
            arr.append(head)
            head = head.next
        if len(arr) == 0:
            return head
        arr = arr[::-1]
        for i in range(len(arr)):
            if i == len(arr) -1:
                arr[i].next = None
                break
            arr[i].next = arr[i+1]
       
        head = arr[0]
        
        
        return head
        
