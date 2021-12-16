class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        temp = [0] * (n + 1)
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                temp[i] = "FizzBuzz"
            elif i % 3 == 0:
                temp[i] = "Fizz"
            elif i % 5 == 0:
                 temp[i] = "Buzz"
            else:
                temp[i] = str(i)
        temp.pop(0)
        return temp
        
