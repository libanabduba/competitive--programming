class Solution:
        
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prevRow = self.getRow(rowIndex - 1)
        row = [1]
        for i in range(1, rowIndex):
            # print(prevRow,rowIndex)
            row.append(prevRow[i-1] + prevRow[i])
        row.append(1)
        return row
