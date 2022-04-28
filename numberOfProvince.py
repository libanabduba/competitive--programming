class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = {}
        for i in range(1,len(isConnected)+1):
            graph[i] = set()
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1 and i != j:
                    graph[i+1].add(j+1) 
                    graph[j+1].add(i+1)
             
        count = 0
        visited = {}
        for i in range(1,len(isConnected)+1):
            visited[i] = False
            
        
        def dfs(node,visited):
            if visited[node] == True:
                return
            visited[node] = True
            
            for i in graph[node]:
                if visited[i] == False:
                    dfs(i,visited)
            
            
        for i in range(1,len(isConnected)+1):
            if visited[i] == False:
                count += 1
                dfs(i,visited)
        
        return count
