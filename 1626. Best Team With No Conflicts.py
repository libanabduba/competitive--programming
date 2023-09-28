class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        pairs = [[scores[i], ages[i]] for i in range(len(scores))]
        pairs.sort()
        memo = {}
        
        
        
        def helper(index, prevIndex):

            if index >= len(scores):
                return 0

            if (index, prevIndex) in memo:
                return memo[(index, prevIndex)]


            maxScore, maxAge = pairs[prevIndex] if prevIndex >= 0 else [0, 0]

            score, age = pairs[index]

            res = 0

            if age >= maxAge:
                res = helper(index + 1, index) + score

            memo[(index, prevIndex)] = max(res, helper(index + 1, prevIndex))

            return memo[(index, prevIndex)]



        return helper(0, float('-inf'))





            
