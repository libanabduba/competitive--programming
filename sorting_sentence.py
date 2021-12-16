class Solution:
    def sortSentence(self, s: str) -> str:
        list = s.split()
        for j in range(len(list) - 1):
            min = j
            for i in range(j,len(list)):
                if list[min][-1] > list[i][-1]:
                    min = i
                else:
                    continue
            list[j],list[min] = list[min],list[j]
        for i in range(len(list)):
            result = list[i].rstrip(list[i][-1])
            list[i] = result

        return " ".join(list)
