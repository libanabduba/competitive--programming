class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def Ispossible(k):
            time = 0

            for val in piles:
                time += ceil(val/k)

            return time <= h

        left = 1
        right = max(piles)
        ans = max(piles)
        while left <= right:
            
            mid = (left + right)//2

            if Ispossible(mid):
                ans = min(ans,mid)
                right = mid -1

            else:
                left = mid + 1

        return ans
