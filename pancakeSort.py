class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        values = []
        def reverse(temp):
            for i in range(0,temp//2 + 1):
                arr[i],arr[temp - i] = arr[temp - i], arr[i]
            
        for i in range(len(arr)-1,0,-1):
            for j in range(1,i+1):
                if arr[j] == i + 1:
                    reverse(j)
                    values.append(j+1)
            reverse(i)
            values.append(i+1)
        return values
            
        
