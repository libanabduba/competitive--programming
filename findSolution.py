"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        arr = []
        array = [i for i in range(1,1001)]
        for x in range(1,1001):
            left = 0
            right = len(array) - 1
             
            while left <= right:
                mid = left + (right - left)//2
              
                if customfunction.f(x,array[mid]) == z:
                    arr.append([x,array[mid]])
                    break
                elif customfunction.f(x,array[mid]) > z:
                    right = mid - 1
                    temp = mid
                else:
                    left = mid + 1
                    right = temp
                    
                
        return arr
