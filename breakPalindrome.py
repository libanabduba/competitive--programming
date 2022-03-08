class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        end = len(palindrome)//2
        arr =[i for i in palindrome]
        if len(arr) == 1:
            return ""
        for i in range(end):
            if arr[i] != "a":
                arr[i] = "a"
                return "".join(arr)
                
               
                
        arr[-1] = "b"
        return "".join(arr)
                
