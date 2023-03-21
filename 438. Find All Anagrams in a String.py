class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []
        left = 0
        right = len(p)
        dic = Counter(p)
        dynamic_dic = Counter(s[left: right])
        ans = [0] if dic == dynamic_dic else []
        
        while right < len(s):
            dynamic_dic[s[right]] = 1 + dynamic_dic.get(s[right],0)
            dynamic_dic[s[left]] -= 1

            if dynamic_dic[s[left]] == 0:
                del dynamic_dic[s[left]]

            left += 1

            if dynamic_dic == dic:
                ans.append(left)

            right += 1

        return ans
