class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        inbound = lambda i, j : 0 <= i < len(mat) and 0 <= j < len(mat[0])

        q = deque()
        visited = set()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    visited.add((i,j))
                    q.append(((i, j), 0))

        
        directions =[[1,0], [-1,0], [0, 1], [0, -1]]


        while q:

            current, path_count = q.popleft()

            for direction in directions:

                new_row, new_col = direction[0] + current[0], direction[1] + current[1]

                if inbound(new_row, new_col) and (new_row, new_col) not in visited:
                    if mat[new_row][new_col] == 1:
                        mat[new_row][new_col] = path_count + 1
                    
                    q.append(((new_row, new_col), path_count + 1))
                    visited.add((new_row, new_col))

        

        return mat
            
