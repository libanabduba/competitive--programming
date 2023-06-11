class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        func = lambda i : -1 * i
        new_stones = list(map(func, stones))
        
        heapify(new_stones)

        while len(new_stones) > 1:
            y = - 1 * heappop(new_stones)
            x = -1 * heappop(new_stones)

            if y != x:
                heappush(new_stones, -1 * (y -x))


        return -1 * new_stones[0] if len(new_stones) > 0 else 0
