class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operators = {"*","/","+","-"}

        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append((tokens[i]))

            else:
                if tokens[i] == "*" and len(stack) >= 2:
                    first = stack.pop()
                    second = stack.pop()
                    result = int(first) * int(second)
                    stack.append(str(result))
                elif tokens[i] == "/" and len(stack) >= 2:
                    if int(stack[-2]) < 0 and int(stack[-1]) > 0:
                        result = ceil(int(stack[-2]) / int(stack[-1]))
                        stack.pop()
                        stack.pop()
                        stack.append(str(result))
                    elif  int(stack[-2]) > 0 and int(stack[-1]) < 0:
                        result = ceil(int(stack[-2]) / int(stack[-1]))
                        stack.pop()
                        stack.pop()
                        stack.append(str(result))
                    else:
                        result = floor(int(stack[-2]) / int(stack[-1]))
                        stack.pop()
                        stack.pop()
                        stack.append(str(result))
                elif tokens[i] == "+" and len(stack) >= 2:
                    first = stack.pop()
                    second = stack.pop()
                    result = int(second) + int(first)
                    stack.append(str(result))
                elif tokens[i] == "-" and len(stack) >= 2:
                    first = stack.pop()
                    second = stack.pop()
                    result = int(second) - int(first)
                    stack.append(str(result))  
        return int(stack[-1])
