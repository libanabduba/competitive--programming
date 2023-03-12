from collections import deque 
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        dic = {}
        for i,val in enumerate(tickets):
            dic[i] = tickets[i]
        
        q = deque(i for i in range(len(tickets)))
        time = 0
        while q:
            curr = q.popleft()
            time += 1
            dic[curr] -= 1
            if dic[curr] == 0 and curr == k:
                break
            if dic[curr] != 0:
                q.append(curr)
        return time
