class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = defaultdict(list)

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        # inbound = lambda i, j: 0 <= i < len(grid) and 0 <= j < len(grid[0])
        visited = set()

        def bfs(src, destination):

            q = deque([src])

            visited = set([src])

            while q:
                node = q.popleft()

                if node == destination:
                    return True


                for neigh in graph[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        q.append(neigh)

            return False

        return bfs(source, destination)


        # rank=[1]*n
        # parent={i:i for i in range(n)}
        # def find(ver):
        #     res=ver
        #     while res!=parent[res]:
        #         parent[res]=parent[parent[res]]
        #         res=parent[res]
        #     return res
        # def union(e1,e2):
        #     pare1=find(e1) 
        #     pare2=find(e2)  
        #     if pare1!=pare2:
        #         if rank[pare1] > rank[pare2]:
        #             parent[pare2] = pare1
        #             rank[pare1] += rank[pare2]
        #         else:
        #             parent[pare1] = pare2
        #             rank[pare2] += rank[pare1]
               
        
        # for u,v in edges:
        #     union(u,v)       
        
        # return find(source)==find(destination)

          

            
