class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)

        if n < 2:
            return arr

        transition = -1

        for i in range(n - 1, 0, -1):
            if arr[i - 1] > arr[i]:
                transition = i - 1
                break


        if transition == -1:
            return arr

        maxi = transition + 1

        for i in range(transition + 1, n):
            if arr[i] >= arr[transition]:
                break
            
            if arr[i] > arr[maxi]:
                maxi = i

        arr[transition], arr[maxi] = arr[maxi], arr[transition]

        return arr

        



    
        
            
