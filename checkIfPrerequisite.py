class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        arr = [[0  if i == j else math.inf for i in range(numCourses) ] for j in range(numCourses)]
        
        for pre,cou in prerequisites:
            arr[pre][cou] = 1
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if arr[i][j] > arr[i][k] + arr[k][j]:
                         arr[i][j] = arr[i][k] + arr[k][j]
                            
        print(arr)
        ans = []
        for pre,que in queries:
            if arr[pre][que] != math.inf and arr[pre][que] != 0:
                ans.append(True)
            else:
                ans.append(False)
                
        return ans
