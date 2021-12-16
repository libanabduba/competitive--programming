class Solution: 
    def select(self, arr, i):
        return arr[i]
    
    def selectionSort(self, list,n):
        #code here
        j = 0
        while j < len(list) - 1:
            min = j
            for i in range(j,len(list)):
                if list[min] > list[i]:
                    min = i
                else:
                    continue
            list[j],list[min] = list[min],list[j]
                    
            j += 1
        return list
