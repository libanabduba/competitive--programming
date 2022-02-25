# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        ans = []
        heapify(heap)
        for i in lists:
            while(i != None):
                heappush(heap,i.val)
                i = i.next
        
        while len(heap) > 0:
            ans.append(ListNode(heappop(heap)))
        if len(ans) == 0:
            return None    
        for i in range(len(ans)):
            try:
                ans[i].next = ans[i+1]
            except IndexError:
                ans[i].next = None
       
        return ans[0]
