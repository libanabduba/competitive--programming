class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        memo = {}

        def recursive_cost(i):
            if i <= 1:
                return cost[i]

            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(recursive_cost(i-1), recursive_cost(i-2))

            return memo[i]
    
        n = len(cost)
        
        return min(recursive_cost(n-1), recursive_cost(n-2))
