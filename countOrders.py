class Solution:
    def countOrders(self, n: int) -> int:
        dp = [1] * n
        
        mod = 10**9 + 7
        for i in range(1,n):
            
            gaps = 2 * i + 1
            ways = (gaps**2) - (gaps*(gaps - 1))/2
            
            dp[i] = (ways * dp[i - 1]) % mod
            
            
        return int(dp[n-1])
