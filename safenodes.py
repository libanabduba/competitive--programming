class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = set()
        cycle = set()
        ans = []
        
        def dfs(index):
            if index in cycle:
                return False
            if index in visited:
                return True
            
            cycle.add(index)
            
            for i in graph[index]:
                if dfs(i) == False:
                    return False
                
            cycle.remove(index)
            visited.add(index)
            ans.append(index)
            
        for i in range(len(graph)):
            dfs(i)
            
        ans.sort()
        
        return ans
            
