class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def helper(arr, minWeight):
            days = 1
            add = minWeight
            for w in weights:
                if add - w < 0:
                    days += 1
                    add = minWeight
                add -= w
            return days
        
        low = max(weights)
        high = sum(weights)
        res = high
        while low <= high:
            mid = low + (high - low)//2

            if helper(weights,mid) > days:
                low = mid + 1
            else:
                res = min(res,mid)
                high = mid - 1
            

        return res
