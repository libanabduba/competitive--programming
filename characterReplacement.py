class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        dic = {}
        size = 0
        l = 0
        for i in range(len(s)):
            
            dic[s[i]] = 1 + dic.get(s[i],0)
            
            if (i - l + 1) - max(dic.values()) > k:
                dic[s[l]] -= 1
                l += 1  
            size = max(size,i - l + 1)
        return size
