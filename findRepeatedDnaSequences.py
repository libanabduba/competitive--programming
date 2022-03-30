class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        seen ,ans = set(),set()
        
        left = 0
        right = 9
        
        while right < len(s):
            
            temp = s[left: right + 1]
            
            if temp in seen:
                ans.add(temp)
            seen.add(temp)
            
            left += 1
            right += 1
            
        return list(ans)
