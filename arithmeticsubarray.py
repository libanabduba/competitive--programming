class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        bol = []
        count = 0
        for i in range(len(l)):
            list = nums[l[i]:r[i] + 1]
            list.sort()
            for j in range(len(list) - 1):
                if list[j+1] - list[j] != list[1] - list[0]:
                    count += 1
                    break
            if count != 0:
                bol.append(False)
                count = 0
                list.clear()
            else:
                bol.append(True)
                list.clear()        
        return bol
                    
