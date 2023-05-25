class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid)

        inbound = lambda i, j: 0 <= i < rows and 0 <= j < cols

        directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[-1,-1],[1, -1]]

        q = deque([([0,0], 1)])
        visited = set((0,0))

        if grid[0][0] == 1:
            return -1

        while q:

            node, path_count = q.popleft()
            print(node)

            if node == [rows-1, cols-1]:
                return path_count

            

            # flag  = False

            for neigh in directions:
                new_row, new_col = neigh[0] + node[0], neigh[1] + node[1]

                if inbound(new_row, new_col) and (new_row,new_col) not in visited and  grid[new_row][new_col] == 0:
                    # flag = True
                    visited.add((new_row,new_col))
                    q.append(([new_row,new_col], path_count + 1))

            # if not flag: return -1

        return -1


        

