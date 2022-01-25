class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        
        stack = []
        j = 0
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j = j + 1

        # return j == len(popped)



        if len(stack) != 0:
            return False
        return True
           
                
            
        
        
        
        
        
