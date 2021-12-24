class Solution:
    def kClosest(self, list: List[List[int]], k: int) -> List[List[int]]:
        arr1 = []
        arr2 = []
    
        for i in range(len(list)):
            if len(arr1) != 0:
                arr1.pop()
                arr1.pop()
            distance = sqrt((list[i][0])**2 + (list[i][1])**2) 
            arr1.append(distance)
            arr1.append(i)
            arr2.append(arr1[:])


        new = sorted(arr2) 
        arr3 = [] 

        for i in range(k):
              arr3.append(list[new[i][1]])

        return arr3
              
