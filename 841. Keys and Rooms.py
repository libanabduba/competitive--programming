class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:



        q = deque([0])

        visited = set([0])


        while q:

            node = q.popleft()

            for neigh in rooms[node]:
                if neigh not in visited and neigh != node:
                    visited.add(neigh)
                    q.append(neigh)

        for i in range(len(rooms)):
            if i not in visited:
                return False

        return True
