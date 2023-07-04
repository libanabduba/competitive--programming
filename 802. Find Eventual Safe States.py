class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
       
        visited = [-1 for i in range(len(graph))]
        arr = [-1 for i in range(len(graph))]
     
        ans = []
       
      
        def dfs(node,visited,stack):
            
            # if not graph[node]:
            #     print("hello")
            #     return True

            visited[node] = -2
            arr[node] = -2
            
           
            for neigh in graph[node]:
                if visited[neigh] == -1:
                    if dfs(neigh,visited,stack) == True:
                        return True 
                if arr[neigh] == -2:
                    return True
     
            arr[node] = -1
            return False
        
        
        
            
            
        
        for i in range(len(graph)):
            if dfs(i,visited,arr) == False:
                        ans.append(i)
            
        ans.sort()
        
        return ans
            
