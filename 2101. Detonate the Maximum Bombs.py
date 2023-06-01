class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        graph = defaultdict(list)

        for i in range(len(bombs)):
            x, y, r =  bombs[i]
            
            for j in range(len(bombs)):
                x1, y1, r1 = bombs[j]

                res = (x1- x) ** 2 + (y - y1) ** 2

                if res >= 0 and res <= (r**2) and i != j:
                    graph[i].append(j)

        # print(graph)

        def dfs(index):
    
            if not graph[index]:
                visited.add(index)
                return
            visited.add(index)

            for neigh in graph[index]:
                if neigh not in visited:
                   dfs(neigh)

        res = 0
        for i in range(len(bombs)):
            visited = set()
            dfs(i)
            res = max(len(visited), res)

        return res
                
