class Solution:
    def tribonacci(self, n: int) -> int:

        memo = {}

        def recur(n):
            if n <= 1:
                return n

            if n == 2:
                return 1
            
            if n in memo:
                return memo[n]

            memo[n] = recur(n - 1) + recur(n - 2) + recur(n - 3)

            return memo[n]

        return recur(n)


