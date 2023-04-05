class Solution:
    def hIndex(self, citations: List[int]) -> int:

        left = 0
        right = len(citations)
        while left <= right:
            mid = left + (right -left)//2
            if citations[-mid] >= mid: 
                left = mid + 1
            else:
                right = mid - 1

        return left - 1

