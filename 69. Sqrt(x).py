class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x

        res = 0
        while left <= right:
            mid = left +(right -left)//2

            squared = mid ** 2
            if squared > x:
                right = mid - 1
            elif squared < x:
                res = mid
                left = mid + 1
            else:
                return mid

        return res
