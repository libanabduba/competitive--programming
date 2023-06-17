class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        rows, cols = len(maze), len(maze[0])

        inbound = lambda i, j: 0 <= i < rows and 0 <= j < cols

        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        q = deque([(entrance, 0)])
        visited = set((entrance[0],entrance[1]))

        exiti = set()

        # Add elements from the first row
        for col in range(cols):
            exiti.add((0, col))

        # Add elements from the last row
        for col in range(cols):
            exiti.add((rows - 1, col))

        # Add elements from the first column
        for row in range(rows):
            exiti.add((row, 0))

        # Add elements from the last column
        for row in range(rows):
            exiti.add((row, cols - 1))


        out = set()
        for i in range(rows):
            for j in range(cols):
                if [i, j] != entrance and (i, j) in exiti and maze[i][j] == ".":
                    out.add((i, j))

        print(exiti)
        print(out)


        

        


        
        while q:

            node, path_count = q.popleft()

            if (node[0], node[1]) in out:
                return path_count


            for neigh in directions:
                new_row, new_col = neigh[0] + node[0], neigh[1] + node[1]

                if inbound(new_row, new_col) and (new_row,new_col) not in visited and  maze[new_row][new_col] == ".":
                    visited.add((new_row,new_col))
                    q.append(([new_row,new_col], path_count + 1))

        return -1


        


        
