class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        inbound = lambda i,j: 0 <= i < rows and 0 <= j < cols

        def dfs(i, j):
            if (
                not inbound(i, j) or
                grid[i][j] == 0 or
                (i, j) in visited
            ):
                return

            visited.add((i, j))
            q.append((i, j, 0))

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        # Find the first island using DFS
        found = False
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break
            if found:
                break

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while q:
            x, y, distance = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if inbound(nx, ny) and (nx, ny) not in visited:
                    if grid[nx][ny] == 1:
                        return distance
                    visited.add((nx, ny))
                    q.append((nx, ny, distance + 1))

