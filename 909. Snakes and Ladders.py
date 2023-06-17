class Solution:
    def getCoordinates(self,cell, n):
        row = (cell - 1) // n
        col = (cell - 1) % n

        # Adjust row and column for the zigzag pattern
        if row % 2 == 1:
            col = n - 1 - col

        return n - 1 - row, col

    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n = len(board)
        target = n * n

        queue = deque([(1, 0)])  # Starting cell (1) with distance 0
        visited = set()

        while queue:
            cell, distance = queue.popleft()

            if cell == target:
                return distance

            for i in range(1, 7):
                next_cell = cell + i

                if next_cell <= target:
                    row, col = self.getCoordinates(next_cell, n)
                    if board[row][col] != -1:
                        next_cell = board[row][col]

                    if next_cell not in visited:
                        queue.append((next_cell, distance + 1))
                        visited.add(next_cell)

        return -1


