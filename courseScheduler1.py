    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ingoing = [0] * numCourses
        outgoing = defaultdict(set)
        
        for course,pre in prerequisites:
            outgoing[pre].add(course)
            ingoing[course] += 1
            
        q = Deque()
        
        for i in range(numCourses):
            if ingoing[i] == 0:
                q.append(i)
        count = 0        
        while q:
            curr = q.popleft()
            count += 1
            
            for node in outgoing[curr]:
                ingoing[node] -= 1
                if  ingoing[node] == 0:
                    q.append(node)
                    
        return count == numCourses
