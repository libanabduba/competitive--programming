class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:


        visited = set()

        ans = []

        def dfs(node, path):

            if node == len(graph) - 1:
                path.append(node)
                if path not in ans:
                    ans.append(path[::])
                return

            # visited.add(node)

            path.append(node)

            for neigh in graph[node]:
                # if neigh not in visited:
                    
                dfs(neigh,path)

                if path:
                    path.pop()

        for i in range(len(graph)):
            dfs(0, [])

        return ans





            
