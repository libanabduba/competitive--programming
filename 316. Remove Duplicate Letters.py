class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []

        for char in s:
            if char in stack:
                count[char] -= 1
                continue
            
            while stack and stack[-1] > char and count[stack[-1]] > 0:
                stack.pop()

            stack.append(char)
            count[char] -= 1
        return "".join(stack)
