class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = defaultdict(int)

        for i in range(len(bills)):
            if bills[i] == 5:
                dic[bills[i]] += 1

            elif bills[i] == 10:
                if dic[5] > 0:
                    dic[5] -= 1
                    dic[bills[i]] += 1

                else:
                    return False

            else:
                if dic[5] > 0 and dic[10] > 0:
                    dic[5] -= 1
                    dic[10] -= 1
                    dic[bills[i]] += 1
                elif dic[5] > 2:
                    dic[5] -= 3
                    dic[bills[i]] += 1
                else:
                    return False

        return True

