class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        length = 0
        left = 0
        right = 0
        myset = set()

        # s = "abcedfchj"

        while right != len(s):
            # # print(left,right)
            # print((left,right), myset)
            if s[right] not in myset:
                myset.add(s[right])
                right += 1
            else:
                length = max(length,len(myset))
                index = s.index(s[right],left,right)
                for i in range(left,index + 1):
                    if s[i] in myset:
                        myset.remove(s[i])
                
                left = index + 1
        
        return max(length,len(myset))

       
       
        
