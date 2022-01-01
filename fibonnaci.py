class Solution:
    def __init__(self):
        self.dict = {0:0,1:1}
    def fib(self, n: int) -> int:
        if n in self.dict:
            return self.dict[n]
        else:
            ans = self.fib(n-1) + self.fib(n-2)
            self.dict[n] = ans
            return ans
