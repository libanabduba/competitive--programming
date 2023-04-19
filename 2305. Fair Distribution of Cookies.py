class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        buckets = [0] * k

        self.ans = float('inf')

        def backtrack(index,buckets):
            if self.ans <= max(buckets):
                return 

            if index >= len(cookies):
                self.ans = min(self.ans, max(buckets))
                return

            

            for i in range(len(buckets)):
                buckets[i] += cookies[index]
                backtrack(index + 1, buckets)
                buckets[i] -= cookies[index]


        backtrack(0,buckets)

        return self.ans
                
