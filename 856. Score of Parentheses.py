class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for par in s:
            if par == "(": stack.append(0)
            else:
                last = stack.pop()
                if last == 0: score = 1
                else: score = last * 2
                stack[-1] += score
        return stack[0]
