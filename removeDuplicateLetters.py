class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
     
        count = Counter(s)
        stack = []
        
        for i in s:
            if i in stack:
                count[i] -= 1
                continue
          
            while stack and stack[-1] > i and count[stack[-1]] > 0:
                stack.pop()
            
            stack.append(i)
            count[i] -= 1
        
        return ''.join(stack)
            
