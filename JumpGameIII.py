class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        dic = defaultdict(set)
        
        inbound = lambda val: val >= 0 and val < len(arr)
        
        for i,val in enumerate(arr):
            if inbound(i- val) and i - val != i:
                dic[i].add(i - val)
            if inbound(i+ val) and i + val != i:
                dic[i].add(i + val)
            
       
        q = deque([start])
        visited = set([start])
        while q:
            node = q.popleft()
            
            if arr[node] == 0: return True
            
            for neighbor in dic[node]:
                if neighbor not in visited:
                    visited.add(neighbor) 
                    q.append(neighbor)
                     
                    
        return False
