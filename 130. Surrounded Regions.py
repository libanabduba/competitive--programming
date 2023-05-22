class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])

        inbound = lambda i, j: 0 <= i < rows and 0 <= j < cols

        directions = [(1,0), (-1,0), (0, 1), (0,-1)]
        
        def dfs(row, col):
            if not inbound(row, col) or board[row][col] == "X":
                return

            board[row][col] = "#"

            for dire in directions:
                new_row, new_col = row + dire[0], col + dire[1]
                
                if inbound(new_row, new_col) and board[new_row][new_col] == "#":
                    continue
                dfs(new_row, new_col)


        for i in range(rows):
            dfs(i, 0)              # First column
            dfs(i, cols - 1)       # Last column

        for j in range(cols):
            dfs(0, j)              # First row
            dfs(rows - 1, j)       # Last row

        # Step 5: Flip 'O' to 'X' and restore '#' to 'O'
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'







