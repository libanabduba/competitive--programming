class Solution:
    def kthLargestNumber(self, list: List[str], k: int) -> str:
        arr1 = []
        arr2 = []

        for i in range(len(list)):
            if len(arr1) != 0:
                arr1.pop()
                arr1.pop()
            temp = int(list[i])
            arr1.append(temp)
            arr1.append(i)
            arr2.append(arr1[:])

        new = sorted(arr2)

        return list[new[-k][1]]
