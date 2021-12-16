class Solution:
    def targetIndices(self, list: List[int], target: int) -> List[int]:
        for j in range(len(list) - 1):
            min = j
            for i in range(j,len(list)):
                if list[min] > list[i]:
                    min = i
                else:
                    continue
            list[j],list[min] = list[min],list[j]
        arr = []
        for i in range(len(list)):
            if list[i] == target:
                arr.append(i)
        return arr
