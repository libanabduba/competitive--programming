class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        inbound = lambda i, j: 0 <= i < len(grid) and 0 <= j < len(grid[0])

        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
   
        def dfs(row, col, visited):
            
            if not inbound(row, col) or grid[row][col] == 0:
                return 0

            if visited[row][col]:
                return 0

            
            visited[row][col] = True
            area = 1
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                
                area += dfs(new_row, new_col, visited)

            return area
            
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j, visited))
        
        return max_area



   
