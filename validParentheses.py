class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        list = []
        for i in s:
            if i in dic.keys():
                list.append(i)
            else:
                if len(list) == 0:
                    return False
                if dic[list[-1]] == i:
                        list.pop()
                else:
                    return False
        if len(list) == 0:
                return True
        return False
                
