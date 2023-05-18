class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1 and i != j:
                    graph[i+1].append(j+1) 
                    graph[j+1].append(i+1)
             
       
        visited = [False] * (len(isConnected) + 1)
            
        def dfs(node,visited):
            if visited[node]:
                return
            visited[node] = True
            
            for i in graph[node]:
                if not visited[i]:
                    dfs(i,visited)
            
        count = 0   
        for i in range(1,len(isConnected)+1):
            if not visited[i]:
                count += 1
                dfs(i,visited)
        
        return count
