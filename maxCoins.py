class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sum = 0
        count = 0
        i = len(piles) - 2
        piles.sort()
        while count < (len(piles)/3):
            sum += piles[i]
            count += 1
            i -= 2
            
        return sum
