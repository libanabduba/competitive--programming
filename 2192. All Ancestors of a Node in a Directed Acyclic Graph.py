class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        
        graph = defaultdict(set)
        ans = [[] for _ in range(n)]
       
        for src,dst in edges:
            graph[dst].add(src)
                    
        def dfs(node,root):
            visited[node] = 1
            
            for neigh in graph[node]:
                if visited[neigh] == 0:
                    ans[root].append(neigh)
                    dfs(neigh,root)
          
           
            
        for i in range(n):
            visited = [0] * n
            dfs(i,i)
            
            
       
        return [sorted(row) for row in ans]
        
        
            
       
           
        
                    
                
            
                
            
            
            
