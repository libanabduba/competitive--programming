class Solution:
    def countGoodNumbers(self, n: int) -> int:

      self.const = (10**9) + 7

      def mod_pow(x, y):
        if y == 0:
            return 1
        if y % 2 == 0:
            p = mod_pow(x, y // 2)
            return p * p % self.const
        else:
            return (mod_pow(x, y - 1) * x) % self.const

      if n % 2 == 0:
          return mod_pow(20, n // 2) % self.const
      else:
          return (mod_pow(20, n // 2) * 5) % self.const
      
