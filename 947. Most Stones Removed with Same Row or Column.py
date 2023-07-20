class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        graph = defaultdict(list)

        visited = set()

        for i, stone1 in enumerate(stones):
            for j in range(i + 1, len(stones)):
                stone2 = stones[j]

                if stone2[0] ==  stone1[0] or stone2[1] == stone1[1]:
                    graph[tuple(stone1)].append(stone2)
                    graph[tuple(stone2)].append(stone1)


        def dfs(node, visited):
            
            visited.add(tuple(node))
            
            count = 1

            for neigh in graph[tuple(node)]:

                if tuple(neigh) not in visited:
                    count += dfs(neigh, visited)

            return count



        count = 0

        for stone in stones:
            if tuple(stone) not in visited:
                ans = dfs(stone, visited)
                if ans != 1:
                    count += (ans - 1)

        
        return count

            

        





            

