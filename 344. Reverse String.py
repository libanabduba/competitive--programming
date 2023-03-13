class Solution:
    def helper(self,s,left,right):
        if left > right:
            return None

        s[left],s[right] = s[right],s[left]

        self.helper(s,left + 1,right - 1)
        
    def reverseString(self, s: List[str]): 
        """
        Do not return anything, modify s in-place instead.
        """
        self.helper(s,0,len(s) - 1)
        
