class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows,cols = len(grid), len(grid[0])

        time, fresh = 0, 0

        inbound = lambda i, j: 0 <= i < rows and  0 <= j < cols

        q = deque()

        # visited = set()

        for i in range(rows):
            for j in range(cols):
                if grid[i] [j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i,j])

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while q and fresh > 0:
            size = len(q)
            rotten_found = False

            for _ in range(size):

                row, col = q.popleft()

                for diri in directions:
                    new_row, new_col = row + diri[0], col + diri[1]

                    if inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        q.append([new_row,new_col])
                        fresh -= 1

                        rotten_found = True

            if rotten_found: time += 1
                        

        return time if fresh == 0 else -1




