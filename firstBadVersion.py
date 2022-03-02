
class Solution:
    def firstBadVersion(self, n: int) -> int:
      
        left=1
        right=n
        while left<=right:
            mid = (left+right)//2
            if(left==right):
                return left
            elif(isBadVersion(mid)==True):
                right=mid
            elif(isBadVersion(mid)==False):
                left=mid+1
           
