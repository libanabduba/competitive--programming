class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1)

        if len(s1) > len(s2):
            return False

        dic_count = Counter(s2[left:right])
        s1_dic = Counter(s1)
        # print(dic_count)
        if dic_count == s1_dic:
            return True 

        while right < len(s2):
            dic_count[s2[right]] = 1 +  dic_count.get(s2[right],0)
            dic_count[s2[left]] -= 1

            if dic_count[s2[left]] == 0:
                del dic_count[s2[left]]

            left += 1
            # print(dic_count)
            if dic_count == s1_dic:
                return True

            right += 1

        return False
