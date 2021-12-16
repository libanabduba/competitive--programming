class Solution:
    def sortColors(self, list: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for j in range(len(list) - 1):
            min = j
            for i in range(j,len(list)):
                if list[min] > list[i]:
                    min = i
                else:
                    continue
            list[j],list[min] = list[min],list[j]

        print(list)
