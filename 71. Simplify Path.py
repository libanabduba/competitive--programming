class Solution:
    def simplifyPath(self, path: str) -> str:
        places = [char for char in path.split("/") if char != "." and char != ""]
        stack = []
        for sub in places:
            if sub == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(sub)

        return "/" + "/".join(stack)
