class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(row,col):
            image[row][col] = newColor
            
            for direct in Direction:
                newRow, newCol = row + direct[0], col + direct[1]
                if not in_bound(newRow,newCol) or image[newRow][newCol] != start_color:
                    continue
                dfs(newRow,newCol)
                
        
        start_color = image[sr][sc]
        in_bound = lambda row,col: 0 <= row < len(image) and 0 <= col < len(image[0])
        # image[sr][sc] = newColor
        Direction = [[0,1], [1,0], [-1,0],[0,-1]]
        if newColor == start_color:
            return image
        dfs(sr,sc)
        return image
                
