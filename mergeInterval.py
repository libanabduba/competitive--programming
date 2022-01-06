class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
         
        arr = []
        if len(intervals) == 1:
                arr.append(intervals[0])
                return arr
        intervals.sort()
        for i in range(len(intervals)):
            if len(arr) != 0:
                if arr[-1][1] >= intervals[i][0]:
                    if arr[-1][1] <= intervals[i][1]:
                        arr.append([arr[-1][0],intervals[i][1]])
                        arr.pop(-2)
                        continue
                       
                    else:
                        continue
                else:
                    arr.append(intervals[i])
                    
                   
            else:
                arr.append(intervals[i])
        return arr
                    
