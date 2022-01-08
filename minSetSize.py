class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = 0
        sum = 0
        dic = {}
        tempList = []
        for i in  arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in dic.values():
            tempList.append(i)
            
        tempList.sort(reverse =  True)
        for i in range(len(tempList)):
            sum += tempList[i]
            count += 1
            if sum >= len(arr)/2:
                break
            else:
                continue
        return count

                
