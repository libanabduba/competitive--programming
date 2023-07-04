class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        graph = defaultdict(list)
        indegree = [0] * len(quiet)

        result =  [i for i in range(len(quiet))]
       

        for rich, poor in richer:
            graph[rich].append(poor)
            indegree[poor] += 1
        
        q = deque()

        for node, degree in enumerate(indegree):
            if degree == 0:
                q.append(node)

        # print(q)

        while q:

            current = q.popleft()

            for neigh in graph[current]:
                indegree[neigh] -= 1

                if quiet[result[neigh]] > quiet[result[current]]:
                    result[neigh] = result[current]

                if indegree[neigh] == 0:
                    q.append(neigh)

        return result

       


        



